from GrabzIt import GrabzItImageOptions
from GrabzIt import GrabzItClient
import os
import telegram_send
from datetime import datetime
from PIL import Image

# Image configuration
grabzIt = GrabzItClient.GrabzItClient("MjM5MzRiYzBlYTRkNGQzMzgyYzg4ZTEyYzc2NDBjNDk=", "Pz8/PzcNV14WWT8/fT0zYz8JP0w/Dj8kPz8rPz96Zz8=")
options = GrabzItImageOptions.GrabzItImageOptions()
options.format = "png"
options.targetElement = "#avisos-interes"
options.browserHeight = -1
options.width = -1
options.height = -1

if __name__ == "__main__":

    # Get date and time
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")

    # Grab new image (https://grabz.it/)
    grabzIt.URLToImage("https://www.comunidad.madrid/servicios/salud/2019-nuevo-coronavirus", options)
    grabzIt.SaveTo("new_result.png")

    im1 = Image.open('new_result.png')
    im2 = Image.open('result.png')

    if list(im1.getdata()) == list(im2.getdata()):
        os.remove("new_result.png")
        msg = "{}\nSin novedades.".format(dt_string)
        telegram_send.send(conf="covid.conf", messages=[msg])
    else:
        os.rename("new_result.png", "result.png")
        with open("result.png", "rb") as image:
            msg = "Novedades!"
            telegram_send.send(conf="covid.conf", messages=[msg], images=[image])
            