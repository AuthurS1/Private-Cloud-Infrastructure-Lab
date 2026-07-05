from ssh_client import SSHClient
from utils.logger import logger

class Monitor:

   def __init__(self, server):
       self.ssh = SSHClient(server)

   def hostname(self):
       output, error = self.ssh.execute("hostname")
       return output

   def uptime(self):
       output, error = self.ssh.execute("uptime")
       return output



   def cpu(self):
       output, error = self.ssh.execute(
          "top -bn1 | grep 'Cpu(s)' | awk '{print $2}'"
       )
       return output.strip()
   def cpu_usage(self):
       output, error = self.ssh.execute(
          "vmstat 1 2 | tail -1 | awk '{print 100-$15}'"
       )
       return output.strip()



   def memory(self):
       output, error = self.ssh.execute(
          "free -h | awk 'NR==2 {print $3 \" / \" $2}'"
       )
       return output.strip()
   def memory_usage(self):
       output, error = self.ssh.execute(
          "free | awk '/Mem:/ {printf(\"%.0f\",$3/$2*100)}'"
       )
       return output.strip()



   def disk(self):
       output, error = self.ssh.execute(
          "df -h / | awk 'NR==2 {print $3 \" / \" $2 \" (\" $5 \")\"}'"
       )
       return output.strip()
   def disk_usage(self):
       output, error = self.ssh.execute(
          "df -h / | awk 'NR==2 {gsub(\"%\",\"\",$5); print $5}'"
       )
       return output.strip()



   def nginx(self):
       output, error = self.ssh.execute(
          "systemctl is-active nginx"
       )
       if output.strip() == "active":
          return " Running "
       return " Stopped "

   def ip_address(self):
       output, error = self.ssh.execute("hostname -I")
       return output
   def gateway(self):
       output, error = self.ssh.execute("ip route | grep default")
       return output
   def dns(self):
       output, error = self.ssh.execute("cat /etc/resolv.conf")
       return output
   def open_ports(self):
       output, error = self.ssh.execute("ss -tuln")
       return output

   def close(self):
       self.ssh.close()

   def start_nginx(self):
       output, error = self.ssh.execute(
          "sudo systemctl start nginx"
       )
       return output, error

   def stop_nginx(self):
       output, error = self.ssh.execute(
          "sudo systemctl stop nginx"
       )
       return output, error

   def restart_nginx(self):
       logger.info("Restart nginx")

       output, error = self.ssh.execute(
          "sudo systemctl restart nginx"
       )
       return output, error
   def mariadb(self):
       output, error = self.ssh.execute(
          "systemctl is-active mariadb"
       )
       if output.strip() == "active":
           return "Running"
       return "Stopped"

   def start_mariadb(self):
       output, error = self.ssh.execute(
          "sudo systemctl start mariadb"
       )
       return output, error

   def stop_mariadb(self):
       output, error = self.ssh.execute(
          "sudo systemctl stop mariadb"
       )
       return output, error
   def restart_mariadb(self):
       output, error = self.ssh.execute(
          "sudo systemctl restart mariadb"
       )
       return output, error

#==============================================
#                  Docker
#==============================================

   def docker_ps(self):
       output, error = self.ssh.execute(
           "docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}'"
       )
       return output
   def docker_ps_all(self):
       output, error = self.ssh.execute(
           "docker ps -a --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}'"
       )
       return output
   def docker_start(self,container):
       return self.ssh.execute(
           f"docker start {container}"
       )
   def docker_stop(self, container):
       return self.ssh.execute(
           f"docker stop {container}"
       )
   def docker_restart(self, container):
       return self.ssh.execute(
           f"docker restart {container}"
       )
   def docker_logs(self, container):
       output, error = self.ssh.execute(
           f"docker logs --tail 20 {container}"
       )
       return output
   def docker_stats(self):
       output, error = self.ssh.execute(
           "docker stats --no-stream --format 'table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.MemPerc}}'"
       )
       return output
   def docker_images(self):
       output, error = self.ssh.execute(
           "docker image ls --format 'table {{.Repository}}\t{{.Tag}}\t{{.ID}}\t{{.Size}}'"
       )
       return output
   def docker_networks(self):
       output, error = self.ssh.execute(
           "docker network ls"
       )
       return output
   def docker_volumes(self):
       output, error = self.ssh.execute(
           "docker volume ls"
       )
       return output
   def docker_inspect(self, container):
       output, error = self.ssh.execute(
           f"docker inspect {container}"
       )
       return output
   def docker_version(self):
       output, error = self.ssh.execute(
           "docker --version"
       )
       if error.strip():
           return None
       return output.strip()
   def docker_container_count(self):
       output, error = self.ssh.execute(
           "docker ps -aq | wc -l"
       )
       return output.strip()
   def docker_image_count(self):
       output, error = self.ssh.execute(
           "docker image ls -q | wc -l"
       )
       return output.strip()
   def docker_network_count(self):
       output, error = self.ssh.execute(
           "docker network ls -q | wc -l"
       )
       return output.strip()
   def docker_volume_count(self):
       output, error = self.ssh.execute(
           "docker volume ls -q | wc -l"
       )
       return output.strip()

