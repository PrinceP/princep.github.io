---
title: "Formats of Image reads"
description: Introduction for the various formats in image reads 
toc: true
comments: true
layout: post
categories: [OpenCV, TensorRT]
image: images/bazel_logo.png
author: Prince
---

# Introduction

Whenever we read images from OpenCV and pass it in Tensorrt for single batch or multiple batch inference, we need to follow the format of NCHW and NHWC.
In this post, we will try to take a deeper look into the correct procedure on how to do that.





# Acknowledgements

[Memory Formats](https://oneapi-src.github.io/oneDNN/dev_guide_understanding_memory_formats.html)
[CNTK Transforms](https://docs.microsoft.com/en-us/cognitive-toolkit/Archive/CNTK-Evaluate-Image-Transforms)
[CNBlogs](https://www.cnblogs.com/morganh/articles/13150131.html)
