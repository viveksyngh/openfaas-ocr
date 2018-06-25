# openfaas-ocr
 Tesseract OCR function for OpenFass
 
Tesseract is an optical character recognition engine for various operating systems. It is free software, released under the Apache License, Version 2.0, and development has been sponsored by Google since 2006. 
In 2006 Tesseract was considered one of the most accurate open-source OCR engines then available.

*Note: Input for this is an URL or base64 encoded string of image with .jpg, .jpeg or .png extension.*

### Usage

Deploy:

```bash
$ faas-cli deploy -f ./stack.yml --gateway=http://<GATEWAY-IP> 
```
OR

```bash
$ faas-cli deploy --image=viveksyngh/openfaas-ocr --name=openfaas-ocr --gateway=http://<GATEWAY-IP>
```


Invoke: 
```bash
$ echo -n 'https://www.pyimagesearch.com/wp-content/uploads/2017/06/tesseract_header.jpg' | faas-cli invoke openfaas-ocr --gateway=<GATEWAY-IP>
```

Output:
  ```
  Noisy image
  to test
  Tesseract OCR
  ```
  
### Sample Image
![True](https://github.com/viveksyngh/openfaas-ocr/blob/master/screens/tesseract_header.jpg)

### Example
![True](https://github.com/viveksyngh/openfaas-ocr/blob/master/screens/openfaas-ocr.png)

