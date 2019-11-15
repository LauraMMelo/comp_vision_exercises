# Computer Vision Exercises

Solução para o teste de Visão Computacional

## 0) Dependências
OpenCV -v=4.0.0
tkinter -v=8.6


##  1) Optical flow e tracking

O script `Optical_flow.py` roda o cálculo do Fluxo óptico esparso pelo método Lucas Kanade. Passos:

1. No terminal, na pasta raiz do repositório, rodar `python Optical flow.py`. A webcam tirará uma foto.
2. Use o mouse para demarcar um retângulo com o objeto a ser traçado. 1 clique para iniciar, 1 clique para finalizar. 
3. Pressione 'c'. O objeto será rastreado.
4. Pressione Ctrl+c no terminal para parar.

##  2) Image Stitching

O script `Image_stitching.py` realiza o stitching. Passos:

1. No terminal, na pasta raiz do repositório, rodar `python Image_stitching.py`. 
2. Selecione na janela que aparecer as imagens que deseja costurar e pressione Abrir.
3. A imagem costurada aparecerá na tela e salvará um arquivo `output.png`

##  3) Object Detection

O script `Object_detection.py` roda a YOLOv3-tiny através do módulo Deep Neural Network do OpenCV. 
A YOLO possui uma série de arquiteturas disponíveis, todas treinadas no COCO Dataset trainval, chegando a uma
performance de até 57.9 *mean average precision* para a YOLOv3-608 e de 60.6 para a YOLOv3-spp, no COCO Dataset test-dev, 
ambas podendo rodar a 20 FPS em uma GPU Pascal Titan X. No entanto, devido aos recursos 
limitados do computador onde estes exemplos foram desenvolvidos, a YOLOv3-tiny foi escolhida.

A YOLOv3-tiny consegue uma performance de 33.1 mAP e pode rodar até 220 FPS. O computador onde este 
script foi desenvolvido conseguiu 4 FPS, e possui as seguintes specs:

- Intel Core i3-5005 @ 2GHz
- 12Gb Memória RAM
- GPU Integrada (Não utilizada neste script)


1. No terminal, na pasta raiz do repositório, rodar `python Object_detection.py`. Uma janela com a webcam aparecerá. Tente pôr objetos como celular ou uma caneca na frente da câmera.
2. Para encerrar pressione 'c'. O terminal imprimirá um relatório simples com a taxa de FPS durante o script.

