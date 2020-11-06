from google_images_download import google_images_download   #importando a lib

busca = "wallpaper"
limite = "30"
salvarEm = "ImagensBaixadas"

resposta = google_images_download.googleimagesdownload()   #instanciação de classe

#criando lista de argumentos
argumentos = {"keywords":busca, "limit":limite, "print_urls":True, "delay":3,"output_directory":salvarEm, "prefix":busca}

paths = resposta.download(argumentos)   #passando os argumentos para a função
print(paths) #imprimir caminhos absolutos das imagens baixadas