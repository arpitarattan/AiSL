# AiSL
Models for text to ASL and back built for CatapultHacks, where we won Best Social Impact Prize. My contribution was building these two models.

![helloasl](https://github.com/user-attachments/assets/2370e32f-212f-43bc-ae4c-df507d20a862)
# Text-to-ASL and ASL-to-Text Pipeline  

This repository contains the implementation of a dual pipeline system that bridges the gap between text and American Sign Language (ASL). The project features two key models:  
1. **Text-to-ASL Generative Image Model** (using a Variational Autoencoder).  
2. **ASL-to-Text Classification Pipeline** (fine-tuned ResNet-based classifier).  

---

## 🚀 Features  

- **Text-to-ASL Generator**:  
  - Generates realistic ASL hand gesture images from text inputs.  
  - Built using a Variational Autoencoder (VAE) with an enhanced two-stage learning process:  
    1. **Representation Learning**: Learns latent representations of ASL hand gesture images.  
    2. **Conditional Embedding**: Embeds text labels into the encoder, producing embeddings that guide the decoding process to generate the appropriate ASL gestures.  

- **ASL-to-Text Classifier**:  
  - Converts ASL images back into text using a fine-tuned ResNet.  
  - Optimized for high accuracy and robust classification even in noisy or occluded scenarios.  

---

## 🔬 Models  

### Text-to-ASL Generator  
- **Architecture**: Variational Autoencoder (VAE).  
- **Key Features**:  
  - Conditional embedding of text labels.  
  - Robust latent space representation of ASL gestures.  

### ASL-to-Text Classifier  
- **Architecture**: ResNet (fine-tuned).  
- **Key Features**:  
  - Pretrained on ImageNet and fine-tuned on ASL datasets.  
  - Optimized for small-scale datasets using transfer learning.  

---

## 📊 Results  
![gen](https://github.com/user-attachments/assets/1e4ee427-7f77-41c9-8bb6-037cac6ed48d)

![sigme](https://github.com/user-attachments/assets/c7a26844-7716-4321-8f7f-4d13aeb5d213)

## 💡 Future Work
-  Enhance the VAE with larger datasets and GAN-based refinement for more realistic images.
-  Expand to word based representations instead of letter

    
