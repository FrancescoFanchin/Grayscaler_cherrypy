import cherrypy
import matplotlib.pyplot as plt
from skimage import data
from skimage.color import rgb2gray
import os
from cherrypy.lib import static
from PIL import Image
import numpy as np



class grayscale:

    @cherrypy.expose
    def index(self):
        #main page
        return """
        <html><body>
            <h2>Upload a file</h2>
            <form action="upload" method="post" enctype="multipart/form-data">
            filename: <input type="file" name="myFile" /><br />
            <input type="submit" />
            </form>
        </body></html>
        """
    
    @cherrypy.expose
    def upload(self,myFile):
        #upload page
        #removing old files
        os.system("rm -r download upload; mkdir download upload")
        
        #preserving file extension in uploaded image
        upload_path = os.path.dirname(__file__)
        ext=os.path.splitext(myFile.filename)[1]
        upload_filename = 'saved'+ext
        upload_file = os.path.normpath(
            os.path.join(upload_path,"upload", upload_filename))
            
        #reading data
        size = 0
        with open(upload_file, 'wb+') as out:
            while True:
                data = myFile.file.read(8192)
                if not data:
                    break
                out.write(data)
                size += len(data)
                
        #html page
        out = '''
        File received.
        Filename: {}
        Length: {}
        Mime-type: {}
        <p>Download the <a href='download'>grayscale version.</a></p>
        ''' .format(myFile.filename, size, myFile.content_type, data)
        return out
        
    @cherrypy.expose
    def download(self):
        #download page
        #retrieving uploaded image
        uploaded_file = [x for x in os.listdir("upload")][0]
        image_input=Image.open("./upload/"+ uploaded_file)
        im =np.asarray(image_input)
        im=im.astype(float)
        
        #converting the image to grayscale
        img=rgb2gray(im)
        fig, ax = plt.subplots()
        ax.remove()
        plt.axis("off")
        plt.imshow(img,cmap='Greys')
        
        #preserving the file extension and saving the image
        ext=os.path.splitext(uploaded_file)[1]
        filename="grayscale"+ext
        img_path=os.path.join("download", filename)
        plt.savefig(img_path)
        
        return static.serve_file(os.path.abspath(img_path), 'application/x-download',
                                 'attachment', filename)
    
        
if __name__ == '__main__':
    config = {'server.socket_host': '0.0.0.0'}
    cherrypy.config.update(config)
    cherrypy.quickstart(cherrypy.Application(grayscale()),'/',{})