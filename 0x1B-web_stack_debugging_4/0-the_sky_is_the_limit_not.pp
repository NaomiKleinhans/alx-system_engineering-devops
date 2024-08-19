# 0-the_sky_is_the_limit_not.pp
# This Puppet manifest optimizes Nginx for high load by adjusting worker settings and keepalive timeout.

exec { 'optimize-nginx':
  command => '/etc/init.d/nginx stop; ulimit -n 65536; echo "worker_processes auto;" >> /etc/nginx/nginx.conf; echo "worker_connections 4096;" >> /etc/nginx/nginx.conf; echo "keepalive_timeout 2;" >> /etc/nginx/nginx.conf; /etc/init.d/nginx start',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'grep -q "worker_processes" /etc/nginx/nginx.conf',
}

# Ensure the nginx service is running after optimization
service { 'nginx':
  ensure => 'running',
  require => Exec['optimize-nginx'],
}
