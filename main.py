import speedtest

speed = speedtest.Speedtest()


print('Download :', speed.download() / (1024*1024), 'Mb/s')
print('Upload : ', speed.upload() / (1024*1024), 'Mb/s')

serverName = []
speed.get_servers(serverName)
print('Ping : ', speed.results.ping)
