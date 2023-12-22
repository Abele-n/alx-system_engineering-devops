#Process killmenow is killed

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
