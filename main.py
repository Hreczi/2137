from dhooks import Webhook, Embed
import datetime
import time

hook = Webhook("tu daj link do webhooka")

print('włączono')

papiezowa = Embed(
    description = 'Papieżowa!',
    color=2137,
    )

img = "https://img.joemonster.org/upload/qok/1320524f8aa4e271421065324509.gif"

img1 = "https://piekarniagrzybki.pl/wp-content/uploads/2017/12/kremowka.jpg"

img2 = "https://c.tenor.com/SuS8w88rMhYAAAAd/mozna-jak.gif"

papiezowa.set_image(img)

papiezowa.set_author(name='21:37!!', icon_url=img1)

koniec = Embed(
    description = 'Koniec papieżowej',
    color = 2138,
)

koniec.set_image(img2)

koniec.set_author(name = '21:38', icon_url=img1)


while True:
    now = datetime.datetime.now().time()

    if now.hour == 21 and now.minute == 37:

        hook.send(embed=papiezowa)
        print('wyslano')

        time.sleep(60)

        hook.send(embed=koniec)

        time.sleep(60)
