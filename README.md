# Prod2GBR

Prod2GBR is a simple tool to allow easy conversion of production file sent by board manufacturers (like pcbway for example)

```shell
python Prod2GBR/main.py -m pcbway -i ~\Downloads\XXXXXXXXXXXXXX.rar
```

This produces a zip file in the same folder of the input file with the correctly named gerber files. Allowing for easy verification