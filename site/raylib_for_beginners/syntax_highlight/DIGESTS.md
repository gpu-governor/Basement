## Subresource Integrity

If you are loading Highlight.js via CDN you may wish to use [Subresource Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity) to guarantee that you are using a legimitate build of the library.

To do this you simply need to add the `integrity` attribute for each JavaScript file you download via CDN. These digests are used by the browser to confirm the files downloaded have not been modified.

```html
<script
  src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.10.0/highlight.min.js"
  integrity="sha384-pGqTJHE/m20W4oDrfxTVzOutpMhjK3uP/0lReY0Jq/KInpuJSXUnk4WAYbciCLqT"></script>
<!-- including any other grammars you might need to load -->
<script
  src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.10.0/languages/go.min.js"
  integrity="sha384-Mtb4EH3R9NMDME1sPQALOYR8KGqwrXAtmc6XGxDd0XaXB23irPKsuET0JjZt5utI"></script>
```

The full list of digests for every file can be found below.

### Digests

```
sha384-1m2pjrOy/Dm/JliuRfZbGdoiP/XAXgZhTh6pRW+O+O0cJm+fBx2+PGqYQUBRJUGx /es/languages/arduino.js
sha384-w9lwucuIeYK8hzWrD0H1CZhvQLisv4eUmJc7pL7oMNkpBVpuuSDAwWJB7XW0ys+z /es/languages/arduino.min.js
sha384-dohVMr/cXV2TKOwUPL+/lGwXDj5WkStqxm1qggnRlXzCoAz5+E7Z29ExXaJt3Gp4 /es/languages/armasm.js
sha384-ocl2WOnIR3HmBi1ZJ2kfjMxq7rNhHxV1t4GFEmTWFMZLbHHXgdhR6HfCneMNCkt2 /es/languages/armasm.min.js
sha384-no5/zgQGupzPFGWV8VpJzfQau5/GI2v5b7I45l6nKc8gMOxzBHfgyxNdjQEnmW94 /es/languages/bash.js
sha384-u2nRnIxVxHkjnpxFScw/XgxNVuLz4dXXiT56xbp+Kk2b8AuStNgggHNpM9HO569A /es/languages/bash.min.js
sha384-qimhSkVWof5rfaFajQk8KAtzSRYyIArcJCMKWdDcNq34F4uplk08wmEyUiYLmO+3 /es/languages/c.js
sha384-5fESKgrRcGs7I/89bn7NKFcHyvIVcmQIG4JfCEAV5Rg5VVtskrmGkHVOIsD1642v /es/languages/c.min.js
sha384-xjI3wQy5aAhTr4JT9bE8tZaEMtNn/fguEQOem1vG04xZl4Ov0uf8bsLkQUoUzvbo /es/languages/cmake.js
sha384-JdSkDmOvEqN4fTPk/zl0QpN/wGh53J+xJRFtOMdEwhZ2iDgT5a/Dl18e/TChDqjK /es/languages/cmake.min.js
sha384-eM9Op3b0ilZ/iW7jeVAMo//MKcEXHCbg1Vf8SMrqds5LIOeF9+3qaX//TsnbItae /es/languages/cpp.js
sha384-+tDHTmLKfBxXgVksRhLEJM4z9PfcGQ2XsrZMDcdJ1SIlPZrtAR4+m4XUX+zJf5nf /es/languages/cpp.min.js
sha384-lU6If27eTyL2Yr+WS3ErF0/raeRKUheLuCM44IUaUshDCTvTeQijobPXY4wgkDGb /es/languages/csharp.js
sha384-k4z6XdU7qI35NxUF8SGumv5kMerrVg/xoat0iSaWnu/dHKoNZKdxZN3gI2WYgMfe /es/languages/csharp.min.js
sha384-dpaRAfrfqLJ/m4qzPviZ8UztzpU27eoBSH+8GjP1nkccMBZ6x9EnnhvlNYMDz0P2 /es/languages/django.js
sha384-xmWxMjSXleWbbNXqoQdpI8OkRJnRmiuJ8cmkovyFJSZxyjycv8DA4XuENvWPDLDk /es/languages/django.min.js
sha384-UprkYUPD60WsGmpla3Npim2r1f0q1YUvuLyap7OkTyFvaGCxjt/RcBDXFxGuFiWA /es/languages/erlang.js
sha384-ffehxKri+ZLFXqRZcDwKHI+OuCy3tWvJDjxmY7kTJNnF4EB//blTQga2gnOuh3UT /es/languages/erlang.min.js
sha384-DRSBRBp34y5KixP9TEkoyASphUQfWiiqtSP20YveUIY05CjkoCG1wOe8A1cfMIZT /es/languages/glsl.js
sha384-0QXwzWESgZAQ8866ALLJEDZ9l14HhJTWnECXBxJ4DHDmywVn0LRIMqz7JJQWG/AM /es/languages/glsl.min.js
sha384-rWXTmRoOwQzy75lNF9TBi7PvwMhKAK+S3iBleDD49aUH8XYtmK8aPZocifjskYny /es/languages/haskell.js
sha384-TaV6bIvb0PAdNigZuAtH9T5CUU7BCEJxOLBsVOeAb4O412gzt++0xyZtxbpQTwcw /es/languages/haskell.min.js
sha384-ZCfS+s/zxY7O2bm2KoVJo1wUrLEpJDHZAi/LJAdJF5XjnfSWICkg6wHd2SEJGpyR /es/languages/java.js
sha384-716dHwZ7zbZcnEwTe7DLxlm5tH3Iyl8vSW5a2kYPgusEdp5k3A3jeZt0Ck+CjYE0 /es/languages/java.min.js
sha384-oQpcUGMBf+VDTHOLQ1uhPp1FgNBo0OZc9gbXGuVFwAogHlkh/Iw6cvKKgcgCQkmV /es/languages/javascript.js
sha384-3T8DJ91yCa1//uY9h8Bo4QLrgEtbz4ILN2x9kSM4QWX9/1kKu6UXC3RAbVQV85UQ /es/languages/javascript.min.js
sha384-R87hRh4kF8+iz2sB6FvLrfR0XZBohjFXeJKIXld1Eji2UVi+M2+OIgJKma/9Ko6u /es/languages/json.js
sha384-QFDPNpqtrgZCuAr70TZJFM4VCY+xNnyGKwJw2EsWIBJOVcWAns9PHcLzecyDVv+x /es/languages/json.min.js
sha384-prYrGnTm7oh5PuKMqLmR+7SrkN+R30qFCvQLyWRjl7bJqveap4Mb3RDeCe84KHSC /es/languages/kotlin.js
sha384-yM8aIXHTDq77S7Ar7r/O8Ix2yH07cPC1z48Qh6HBzcG2+plE8YMQn9goknWvawaH /es/languages/kotlin.min.js
sha384-EUUI6yUHTy79oan3YmaO4JgOeT6F/YxDDPJJSYcyhtSak1GZiPjsR4F/YC5getIP /es/languages/llvm.js
sha384-gpuZNMDkXtGAGcK7Oc23L5g4M6m2q3cDgegXlnpTN7euamQLboWR9c5lPIrINbrq /es/languages/llvm.min.js
sha384-OJrXTVCemUa68axskWVxZHXuDfyPWWFK0X2cJsPaMBt6jGY1HxnBZJVPEHTqou4H /es/languages/lua.js
sha384-cjlU8DPjZ3XY/dLzIx+CaoB2jzKXf43s2KSU2rZQGmxwR1d7k9p+SFt1IsNkFnnV /es/languages/lua.min.js
sha384-npg+R4K6p4Q5dEzYDKy3gZ+l4mGV8hDMErOZdSSvqLxED30Fhmgb54WD4wkeY5yh /es/languages/makefile.js
sha384-Ev1PV0+HiSwEbi0IfJYmpMoxv3E0sWhAALg1frIiitM9zh2BVDe871H9Z/RGXqFM /es/languages/makefile.min.js
sha384-JkFMmKMbHcXjdfHauRnREGG6i73GyMisdqNivBm4Z9m2Oc82YIu5jQtIjLa508e8 /es/languages/markdown.js
sha384-65/lNNIY+ayhHTtFznjnyZ5w2NDdZIpSEcqjss/p4ex5JamZ46FdYwDDf6IBLCmE /es/languages/markdown.min.js
sha384-V9eZnDeyLEChcdw2S4ZrzbR+FjJOlFK9w12EWfFWggNGNQWiKFueS1W5ypgy5Us9 /es/languages/mel.js
sha384-ktem8uFt3dpR7cjM5U2q/rcOhjrg9RTRnjRvEN2Y3X7F7CO2/NI/9fVNhUWqL51+ /es/languages/mel.min.js
sha384-YhFioQq+M459546JNsJ++7mn7+6ZCmkRbUPGL/YBnhckluv7ioTXlsN1q8JV9Nag /es/languages/processing.js
sha384-8KwenjihmQdgtsLsST675iXMgQbH8MZ8M4yyaaUY34BK27FxLwO3t6Vf/XnrTuLN /es/languages/processing.min.js
sha384-e+d8RFZbtc5Pmt3xfX9uuElm63v5qOj7T5hAkkFbnYc1wEk7wCLlzOsm66MCf5Uk /es/languages/python.js
sha384-CPHh+9FxkWF3OtMZdTj5oQN1Qti0p4/5XBABz/JdgssOKHmfAOFz6Gu4tsG6MQiH /es/languages/python.min.js
sha384-+m9n/kKanrxb+bcsIb1RGy95tZ+H79GVfj6sSFdNhA/gZoP5+GZY5tpmiXD7bEc4 /es/languages/rib.js
sha384-/iToU4LYE5K1+u9mjsp4ezWGcJP7+loe1xp2GQbhNepeNtU1a9y1bC3V/hjyP+IC /es/languages/rib.min.js
sha384-6YkpGIxhmTvceWvNhd6BfnOl46kg/1G6RsQTIxKO1Ofypo7ihgT6B57Y/RMO0Q9f /es/languages/rsl.js
sha384-TTaTGhHJtVCiuponl3c3W41yk7oceUGvbthSIf0YIAy1Ua89nyjf3/xROIRa0ZeO /es/languages/rsl.min.js
sha384-LZ+YGF0Xve9sHzC9G37Kc14gDC6lfDpny2hggVJVfHb+OsTEXgMGLmAWUJzi4YRC /es/languages/rust.js
sha384-/ktfWRgwL+kZAZeeXDl9mwkD/3atjwjkzLCCoSHtME7MzP87wMhUmNUZ83AoqYx2 /es/languages/rust.min.js
sha384-VYwyP5ddOUunx1AGpbtE38OKY2PbjW9kk6X6622tvqprRJk6W8/tgMvI7MqaOZZw /es/languages/shell.js
sha384-gRgqaIgHrAR1qlo866rkV1AUahqopv0dnpFFLAC4X3jYTDagRCTxQBTMFGV1+x1U /es/languages/shell.min.js
sha384-ZX3mm6sjLYWMBTMUJYzvQXYHNWVJkD+t1ppx4BysyVs6cVhvYFVuwMlVCeAwtwm9 /es/languages/sql.js
sha384-DloKeCkj/pTPHeqWu3keGoEPpZJGm44yQjSmSfpWasykAMUobM0hcYFFPsg1PE6K /es/languages/sql.min.js
sha384-t1qgoHZHiiSTj6BjC5oaU9wYqedDDwqUHrkKztn2/8Kvy+xxVhs58pHnUlFGWIqZ /es/languages/verilog.js
sha384-3cj0wcUVuyPZD7/NmQZVe+R/5hKUXDXlyokh6aPqJBzdN65LnXrrDuR8JJyNrKvN /es/languages/verilog.min.js
sha384-qMVhj1A6BH7PuDigiBaNE2AYrJ4mImzcMqW+ouM5938g+O7uyaP6ygZcs2uA/mr+ /es/languages/vhdl.js
sha384-mdQMmzz/pL52qaQqnXG63Jewnl+lDaXRUeF60ffBbU45RuinqP9EDGlxzyALbe+/ /es/languages/vhdl.min.js
sha384-BcjZoAx+JfnWI/YaICe1dbsNQwCCBWJKS5uLzyKKMiLTVxBqOIRmaUoiJnYADo0M /es/languages/x86asm.js
sha384-y1FgDrVkuSox/kv/Oib26ZqzunABWyUkirzc4i4sthq8Z7c/ReWp2XA9DCh7MHQh /es/languages/x86asm.min.js
sha384-Tdx2DY9ZTHx3KhVXYqOVKx3q1zOboDGlTTv8sgMlER8y4WETtqL+C4VQ7B4A0OGq /es/languages/xml.js
sha384-n9ZezaAVj8pK1BIFZQxmC1BM9yGuBNRgvsOxHMHPCXzqYd1gSYIu9KjgGEm8K57w /es/languages/xml.min.js
sha384-TRdlxCSNmTNG3v+joTZ5Y4I/4Xf5ii/wekG9tuSxcHAf9BX30vv3+jrD0qR9WXKv /languages/arduino.js
sha384-1fjvRLYZVspF/TsOQHIoipbUkoNfSWsc5/FG6aYc1rnvRhLFDZmjuEJRiRZQBgzb /languages/arduino.min.js
sha384-4/eoaXGY0UlWfANb3jyU/u/F701OSu1vFrwgCsXudMnlDIXGAZ4jffvuyiBgg43d /languages/armasm.js
sha384-Xg2bPVtjGJ1EYwh3oKsNkG6p/YNRk1ZGW9IRCbYfFccqH8e7Lm9JPcFZQnMOzNOr /languages/armasm.min.js
sha384-4SbTAv3AX2fuPCpSv6HW3p07YgA7hFfcwG2zJHtYv0ATIt1juD3IXj2NSYwTeIpm /languages/bash.js
sha384-83HvQQdGTWqnRLmgm19NjCb1+/awKJGytUX9sm3HJb2ddZ9Fs1Bst2bZogFjt9rr /languages/bash.min.js
sha384-WHdxyD51Y+ytDdcYGVkKHQOThUwwhLl/1GvZxHTHL4ImI4NS32L/B8bvB/1zN/Mk /languages/c.js
sha384-jtwnwOYA+K4zYN55fA4z4U0PTK5oEp4RcLYaXkYRKO3UUzge1o21ArmvKmTRdh/d /languages/c.min.js
sha384-gXeNvrs51WLYPI/WV54m5BSGtmPSOkEngcs0hrofwSIZ+uVCXW6SwnU75AWUpsiH /languages/cmake.js
sha384-NXUiKRE4iB8J7h3t1Z2aLjDRJslCWi4SWqJpec1z0Y927kNqWejg1uGaEh1P3GCK /languages/cmake.min.js
sha384-M2wpTxQe2N0750xYZ0zTinwbmjsZjdtuS7twUUP2dxtHR0YqhY3JuUFyyhANf9Uy /languages/cpp.js
sha384-/yf54L01PbO6NtVs1Pu9rgfNHbKXanLdNcGVuNa0m5+KiyH+1NpZRDK6idm5VoVl /languages/cpp.min.js
sha384-73x+NDGuWTdFik2BOd5uwmBcikSmR+Qx5AVbJLifM/M0hBbwKToQ45xBWxKYkpgd /languages/csharp.js
sha384-6NsOlZtv7W2iSoDU+Yi+hENfl3MuiECvnl7emdRUvpIpDbLvoCjpAU1fjE6HxIQp /languages/csharp.min.js
sha384-gfyiMmAn2+1KPBU6zgf5/GuxwAS1MG2sXO2QNIa1b8gWqS+ZAEGASFZUv2DTTr0I /languages/django.js
sha384-E8a05vTFeTlJrGsYy6uvHSN7YyYtYVDfuTB0NYKryrTqkKAh0Kljndtou/5x9KxE /languages/django.min.js
sha384-SlKWu3SvV7MLl/uYjSGXVo0n5bflYsgkvmH8lmKx1XmwA3jKehvoWmuCHcXsMbjj /languages/erlang.js
sha384-0CP4DzMXyug19cwGTs3ONRRpUBBFTa4O5Hv9YjyJY10yvQOl5W+x5LOifval6ZBt /languages/erlang.min.js
sha384-FmsaZHRekzHoNL++5S8HZFIJNK42khOgzT3VRksnYVHAURRu3hL5xMgenu9lHyAr /languages/glsl.js
sha384-ubPsF/0wBxL7zEYtpuIL27F0zYtzIZknk+3GdMEcQw1v0Td6xAJ6gDhxHy0UFhk+ /languages/glsl.min.js
sha384-fAOcr1krCNXboMwn/cAybBtSHzCLUrlvVfJT4decCiteyOsqee0RnqLS23UiUBNI /languages/haskell.js
sha384-1+L6SezuX8EOUBfYZyp1GMjjPHwIiJhMhRsLebXPt5ItYffwrwQII8OW4Zu/hndV /languages/haskell.min.js
sha384-cZ2d3Mo/jmTF9r2kHWcHmA8hehxX8N44UN6LSkEhaCRe6t8e9ntd5JEuafywm0aw /languages/java.js
sha384-8mc5ynnm3AlnXn8P3ccSqVAaZIDoijPM08/Hp4DABy6GMy7EHCQFwiIUoGAaGJiO /languages/java.min.js
sha384-p/utwvqrRVOLlz0BjJ0BCGCb2liTDipfz47/QmGXz9hoPIjCKYEgmYUC30VmGgZy /languages/javascript.js
sha384-L/XmDiyusXomLRGcRmcBpPlboRFjpQNV747OJvg+sEOpgGYvUsNwcC4JLNQ2dI6O /languages/javascript.min.js
sha384-psmmPlbfEWGyvRapexDqkVTgNz7Y1xvlGdLNWQSafI4GFQYFDXPZxVXH1laU4n6l /languages/json.js
sha384-Bb6DhE3tUpBROwypL78TbhRUs9QbCt2GxcxVSYglt2l3MefrYkm4CfwjfWhRfQaX /languages/json.min.js
sha384-Ve7wqoYcjaWimhzLnfK0sj2Lij8DmxK2diJ9kazkpifUrd7O+b2CbnHSxD3SCzqj /languages/kotlin.js
sha384-s0inyAR7LE5SVvn9VCZrQaiUxkDi+RsQdSKzFh2CjWf+LFd01DAjt9wtxGhT+4qT /languages/kotlin.min.js
sha384-CAesSA8LQoXhLarhdcoHgorC4QmHI9t5Jn+0n9OWH7aNpeTuQTdsLz4jpR02c1mM /languages/llvm.js
sha384-2E2Olv5Np0C9fY2pt3A6kvYCcGDTyGzMc1HxkVA5d0gczQAz7YiPND12qr1xDfzG /languages/llvm.min.js
sha384-N16TmpAW2Qx3T6s3/C0f0jweUUSh69YsJ1+AnOsAePpjmmydXF/mjeY0MZEF/cPn /languages/lua.js
sha384-WES4Ky9nlehN2gBM6oY3/98hVtWF5PZnBO+7jK8ZVKFo+QR32zhfuRK+Mv9jQsOK /languages/lua.min.js
sha384-Z4QQuz3ChYj9P02v2CDc+Y0OAn3iWXtJnyNd0Q6QqW4GV28viT3zcS9tYSmb9x1L /languages/makefile.js
sha384-pYbMiHWycMKEfJaSEsquFRDTjCY7QHvQN0FIfDK0lVMd9DPJuOA7Kq5wZGecvYwM /languages/makefile.min.js
sha384-TVvUXbmPgdS59xZSFUeyNQ1vUkeCbBpuMj3qlzdEwdQhoO5F/WNdI94UEw8g7Enp /languages/markdown.js
sha384-sFh+6oaRBb6kdaMLf8x7qeH7NTvm2u1Ta6PtI0S8hoA+bP7UtHCyKFzaI1JBXwhT /languages/markdown.min.js
sha384-2YmBKpUO4kz3w014lPthisoqAmgxSKhEYqgP3VBApxkj+XudCSsdN3h8555jmERy /languages/mel.js
sha384-dlO3LB/5yjSdavmxp9TaKZblcqj5zaTJRDKgojwiVYPxMdmAUtAzPQsTW/0haJZJ /languages/mel.min.js
sha384-YyOpJjUHKDExvBHAAZLYGW3flcxbgjI3plJ/wzjTYUZut9XfnUjvPJY6saenN05Y /languages/processing.js
sha384-a+nwjMBrHHj4K59nk1SmGnkQ19/zLAQrOQaVUYsiTcBr+HeKqUrjvw5Znx6HQeS7 /languages/processing.min.js
sha384-WNah6F2QDUbmrNCi0fSEyKJbSb01S1ijnoiwbDnegW7dm2Cz/H1CiH1HhWlUvj01 /languages/python.js
sha384-YDj7s2Wf0QEwarV3OB8lvoNJJCH032vOLMDo2HDrYiEpQ+QmKN+e++x3hElX5S+w /languages/python.min.js
sha384-Hwu7t/Tjfl7JEJSV3LoJXYbOX52UyDBYMsWOo3Cwwnu58AmNmo/SniAE/BOLQvmp /languages/rib.js
sha384-Jc59QIC9wiM+tNA9lnx0Cb23+WrXa6PT2LgOAhVPwyx490IJRKdt9/NGT1ZyQc6y /languages/rib.min.js
sha384-ZnEz0w5YKa4T2FMJP08uWJdNC2bZbrL9jpDeH9vJZRKBqJxwO/8Hl1UjzRc3xg3m /languages/rsl.js
sha384-9rzhEAd8EfJCPELcwmTS0OeWys1RBPz26Oghv+u7GT0oXa1PrDPxfsPU7SHQ3fKn /languages/rsl.min.js
sha384-rCXn7K5j/lD2PrSex2XCqyLKap2Ibnsls0uQCx4ZaezI1FJ5RYvoWcsAl/v8SKlE /languages/rust.js
sha384-VTNxHMz2AmpHxzSm8SvRI0As5+wID2j2XJBFtWTic2iEK8WbXgR1fymVQS9S2DvY /languages/rust.min.js
sha384-KYOeDvyFo8fJObDV1L1aoPnfs6XG68LL6j3INM7McXyRYtBZF7DdUsNjK25dtxKo /languages/shell.js
sha384-olAuUjfRvTi/iEH4RXRpaq/G1iJGizn7OefkyJLQYuqNhh1xAV5dnUrkH/LlPd9j /languages/shell.min.js
sha384-w/OmtgUvmlKWaVatpcvuEQxP7bkJzI5gLeeQkuXjApJNiQvNmXFL2PBM5RWgKqDr /languages/sql.js
sha384-2uzCjI3OPwJce6i2hphsYs1qqTqRrDnfPXbfjZggPWy2/Lgl8gzV9Hyl0jhhoWy4 /languages/sql.min.js
sha384-1JXyk4uCVxAfcJRwRfNnpt8moDWzGVnTnXk4ucnBTXFoDyeEP1/FqjQCqgutU9nc /languages/verilog.js
sha384-i+ovBPuX6/6IYKo/hvzjiDeWmFZGjQ8GcN5P2JlCvsQQz7tmGhwFBZ7L8O5j6Uih /languages/verilog.min.js
sha384-V2Oynheqj/yMT38G4zcskFIWTJwExjl3g3gvD2a0rga9jbrWA1jdlARfXwdxDFeN /languages/vhdl.js
sha384-lRfKmfeanfEEsne7ndto0E7FFUaI9By4vEr1RZkq+pVhHu4dRKebAURBKne7Dzdm /languages/vhdl.min.js
sha384-9s/ZvqYSxQS2hJrT3LuFUwDyxlWEELd50mRuGXt0zzSwafBqEWPsv9xxNsZUF2W4 /languages/x86asm.js
sha384-cw6YAmvOjrczJAb9NkjJRzsXso0VEJrJsLZl8G49s9vVlIFVwG8cR6K8yvpDlGn5 /languages/x86asm.min.js
sha384-QAL2h4IMgQaJUJjUy0dSWdAut7o/A272ai8qOsJ8SSm9KMxkdLgH7oGfLGft/EJ0 /languages/xml.js
sha384-CN3No+n1UZXCFYyl+ge5yAPGTNGuH23BdIsFJxntDmEYL94AmoZlNBHGSdjVSjKG /languages/xml.min.js
sha384-GGkEVBk3+6dtou5NGMrLXa8MDiWxHeXtccMmgdpdVNhBV7UTfoqhpkXiZtd3N5Fc /highlight.js
sha384-Mc/+6ahpabd0qbr6XdN3Up4OzJHtsrgINOpqaXJoUBVrkOlqF5zLkM+Qp09g/TUJ /highlight.min.js
```

