from pygal.maps.world import World
'''
绘制世界地图
pygal_maps_world 1.0.2
'''
wm = World()
wm.force_uri_protocol = 'http'
wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
    'gy', 'pe', 'py', 'sr', 'uy', 've'])
    
wm.render_to_file('../img/americas.svg')
