# onlinestorecompare
A flask API to search major nigerian online stores to compare prices.
currently supported nigerian stores:
* Jumia
* Konga
* Jiji
* Kara
* Slot
---
## Flask API endpoint 
_https://onlinestorecompare.herokuapp.com/search/<term>_
  
  ### Sample Request 
  > [https://onlinestorecompare.herokuapp.com/search/infinix hot 6]        
  (https://onlinestorecompare.herokuapp.com/search/infinix%20hot%206)

  ### Sample Response 
   ```[{"image":"https://ng.jumia.is/Br14qleqL2_5kzFxXPfAybKxdtc=/fit-  in/220x220/filters:fill(white):sharpen(1,0,false):quality(100)/product/56/848812/1.jpg? 1026","price":"41500","source":"jumia","title":"X606B 16GB Rom + 2GB Ram","url":"https://www.jumia.com.ng/infinix-x606b-16gb-rom-2gb-ram-21884865.html"},{"image":"https://ng.jumia.is/3a4LyceoLsK3d94DlO9JaIjnZJc=/fit-in/220x220/filters:fill(white):sharpen(1,0,false):quality(100)/product/60/494912/1.jpg?1246","price":"35500","source":"jumia","title":"Hot 6 (X606D) 6-Inch HD+ (1GB RAM, 16GB ROM) Android 8 Oreo, 13MP + 8MP Dual SIM 4G Smartphone - Blush Gold (BF18)","url":"https://www.jumia.com.ng/infinix-hot-6-x606d-6-inch-hd-1gb-ram-16gb-rom-android-8-oreo-13mp-8mp-dual-sim-4g-smartphone-blush-gold-bf18-21949406.html"},...```
  
## Vue.Js Front-End
_https://onlinestorecompare.herokuapp.com_
[OnlineStoreCompare](https://onlinestorecompare.herokuapp.com "OnlineStoreCompare Front-End")
> Enter the search text in the box provided and click search, it will return results from lowest price to highest


### Contributions are welcome
