# GANArt: Using AI to create Portraits

![Sample_gif](images/sample.gif)

GAN(Generative Adversarial Network) is no wonder an amazing discovery in the field of Deep Learning. From generating fake human faces to an entirely new virtual world, if there is room for creativity, one can indeed implement GAN. This fascination of mine towards Generative Modelling, and in particular GAN, led me towards this creative project.        

There are many works already where people have applied GAN in the field of Arts, from abstract arts to genre-specific paintings(using <i>Conditional GANs</i>), and some of these works inspired me to dig deeper into the field of GAN.

For this project, I have used Nvidia's [StyleGAN2 ADA model](https://arxiv.org/pdf/2006.06676.pdf), StyleGAN2 is an upgraded version of its earlier model [StyleGAN](https://arxiv.org/pdf/1812.04948.pdf), as we know training a GAN using too little data typically leads to discriminator overfitting, causing training to diverge, and therefore, Nvidia came up with the idea of adaptive discriminator augmentation (ADA) and solved the issue of discriminator overfitting.