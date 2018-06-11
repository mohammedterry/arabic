import cherrypy,os,arabic

class Arabic:
    def index(self):
        query = '''<br><br><br>A (ع)<br>g (غ)<br>H (ح)<br>x (ة)<br>T (ط)<br>S (ص)<br>D (ض)<br>...<br>
            <form action="results_page" method="GET">
            <br> transliterate: <br><br>
            <input type = "text" name="name" /><br><br>
            <input type="submit" />
            </form>
            alsalaamu Aalaykum waraHmaxu lllahi wabarakaatuhu<br><br>l-salāmu 'alay-kum wa-raḥmahu llahi wa-barakātuhu<br><br>الْسَلَامُ عَلَيْكُمْ وَرَحْمَةُ لْلَّهِ وَبَرَكَاتُهُ
            '''
        return query
    index.exposed = True

    def results_page(self,name=None):
        tr,ar = arabic.arabicize(name)
        results = '{}<br><br>{}<br><br>{}'.format(name,tr,ar)
        query = '''<br><br><br>A (ع)<br>g (غ)<br>H (ح)<br>x (ة)<br>T (ط)<br>S (ص)<br>D (ض)<br>...<br>
            <form action="results_page" method="GET">
            <br> transliterate: <br><br>
            <input type = "text" name="name" /><br><br>
            <input type="submit" />
            </form>
            '''
        return query + results 
    results_page.exposed = True

cherrypy.config.update({'server.socket_host':'0.0.0.0'})
cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', 5000))})
cherrypy.quickstart(Arabic(), '/')
