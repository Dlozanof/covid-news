from GrabzIt import GrabzItImageOptions
from GrabzIt import GrabzItClient
import hashlib
import os
import telegram_send
from datetime import datetime

# Image configuration
grabzIt = GrabzItClient.GrabzItClient("MjM5MzRiYzBlYTRkNGQzMzgyYzg4ZTEyYzc2NDBjNDk=", "Pz8/PzcNV14WWT8/fT0zYz8JP0w/Dj8kPz8rPz96Zz8=")
options = GrabzItImageOptions.GrabzItImageOptions()
options.format = "png"
options.targetElement = "#avisos-interes"
options.browserHeight = -1
options.width = -1
options.height = -1

# Hash configuration
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

if __name__ == "__main__":

    # Get date and time
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")

    # Grab new image
    grabzIt.URLToImage("https://www.comunidad.madrid/servicios/salud/2019-nuevo-coronavirus", options)
    grabzIt.SaveTo("new_result.png")

    if (md5("new_result.png") == md5("result.png")):
        os.remove("new_result.png")
        msg = "Sin novedades [{}]".format(dt_string)
        telegram_send.send(messages=[msg])
    else:
        os.rename("new_result.png", "result.png")
        with open("result.png", "rb") as image:
            msg = "Novedades!"
            telegram_send.send(messages=[msg], images=[image])