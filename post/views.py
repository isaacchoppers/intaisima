from django.shortcuts import render
from datetime import datetime
now = datetime.now().strftime("%b %dth, %Y - %H:%M hrs ")

posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    },
    {
        'title': 'El arte de la guerra',
        'user': {
            'name': 'sun tzu',
            'picture': 'https://www.bing.com/images/search?view=detailV2&ccid=u7nQUNnU&id=D86C4DF5FBB7FBCF4C50793C30DC35711C534A5D&thid=OIP.u7nQUNnU00q-Liwe_-AbeQHaLI&mediaurl=https%3a%2f%2fupload.wikimedia.org%2fwikipedia%2fcommons%2f3%2f37%2fEnchoen27n3200.jpg&exph=1024&expw=681&q=sun+tzu&simid=608034856347895006&ck=A8C7C25B6CA1270A85F28AE775EE1C90&selectedIndex=0&ajaxhist=0'
        },
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://www.bing.com/images/search?view=detailV2&ccid=gHggHAd0&id=C6FCE3D0494D1B7C93A4E205EFA4D32D91BCAAA0&thid=OIP.gHggHAd0gR3_9yKXNnJbZwHaJ7&mediaurl=https%3a%2f%2fimagessl4.casadellibro.com%2fa%2fl%2ft0%2f34%2f9788441532434.jpg&exph=1341&expw=1000&q=el+arte+de+la+guerra+tzu+sun&simid=608025845477084535&ck=8344B6C7B6157A9860536BA3D302CEF7&selectedindex=0&ajaxhist=0&first=1&scenario=ImageHoverTitle',
    },
    {
        'title': 'El arte de inovar',
        'user': {
            'name': 'Mario Borghino',
            'picture': 'https://www.bing.com/images/search?view=detailV2&ccid=b6v9eeQ6&id=54966A36D8245748EB06A849653F8FC4360FFF3D&thid=OIP.b6v9eeQ6nVw7DALzyL5bVwHaHa&mediaurl=https%3a%2f%2fyt3.ggpht.com%2fa%2fAGF-l78iB_sHTZ3_VwIMT50Dv-TNhpNsRL7Q3y7A7A%3ds900-c-k-c0xffffffff-no-rj-mo&exph=900&expw=900&q=mario+borghino&simid=608005435769294013&ck=871B51555E5A5F9E76AC4DB71A401BFF&selectedindex=0&ajaxhist=0&first=1&scenario=ImageHoverTitle'
        },
        'timestamp':datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://www.bing.com/images/search?view=detailV2&ccid=OGn9T6p6&id=C3DDBCD7290F622544F98C241409347483A880DD&thid=OIP.OGn9T6p6UUu-M34M2dueSQHaIc&mediaurl=https%3a%2f%2f4.bp.blogspot.com%2f-oVFzoDgfK0Q%2fV1ilvicYqPI%2fAAAAAAAAD6o%2foPA4D7GkdA0ZqC4gBy5mic5xcWd0qzR4ACLcB%2fs1600%2fINNOVAR%252BMARIO%252BBORGHINO.png&exph=570&expw=500&q=mario+borghino+libros&simid=608009949862889628&ck=335DAD3F86580825DDFF32ABC33A7B94&selectedIndex=8&ajaxhist=0',
    }


]
# Create your views here.
def list_posts(request):
	return render(request, 'feed.html',{'posts':posts})

	