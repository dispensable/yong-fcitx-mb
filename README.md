# yong-fcitx-mb
永码(yong/小小输入法) fcitx 码表

虽然小小很好用，但是telegram怎么都用不上小小输入法，没办法只能装个fctix凑合，但是辅助码不熟悉真的打字非常的痛苦。所以直接把小小的永码的码表弄到fctix里直接用舒服一点。

# 使用
1. 安装 `fcitx-table`: `apt-get install fcitx-table`
2. cd 到项目, make env && make mb
3. `cp yong/yong.conf yong/yong.mb ~/.config/fcitx/table/`
4. 重启输入法生效

# ref

1. [码表输入法](http://fcitx.github.io/handbook/sect1-code-table.html)
2. [小鹤码表](https://github.com/rydesun/fcitx-table-flypy)
