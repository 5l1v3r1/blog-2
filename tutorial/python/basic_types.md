# 基本类型

## 目录

- 安装
    - [Linux](./linux.md)
    - [Windows](./windows.md)
    - [macOS](./macos.md)
- [Hello World!](./hello_world.md)
- [基本类型](./basic_types.md)
- [容器类型](./composite_types.md)
- [控制流](./flow.md)
- [函数](./function.md)
- [面向对象编程](./oo.md)
- [面向接口编程](./interface.md)
- [模块和包](./module_and_package.md)
- [异常处理](./exception.md)

---

正如同大部分的编程语言都有整型、浮点数、字符串等等，Python当然也有。不过与其他语言，例如 [Golang](https://jiajunhuang.com/tutorial/golang/basic_types.md)
的不同，Python中的类型简单多了，也好用多了。如果你学过C、Go语言等等，就会知道，整型有 `int`, `int8`, `int16`... 好多种。

Python中可没有这么复杂，就一种：`int`。而浮点数也是这样，只有一种：`float`，字符串是 `str`。布尔类型是 `bool`。接下来，我们分别和他们打个招呼。

> 除此之外，还有就是不那么常用的，复数(`complex`)。

首先我们在命令行输入 `python`，然后回车，接着我们输入数字1，字符串"Hello"，浮点数(就是我们平时说的小数)，看看Python中他们分别长什么样：

```bash
$ python
>>> 1
1
>>> "Hello"
'Hello'
>>> 1.234
1.234
>>> type(1)
<class 'int'>
>>> type("Hello")
<class 'str'>
>>> type(1.234)
<class 'float'>
>>>
```

> 在Python中，我们使用 `type` 来检测，或者说输出一个变量的类型。关于什么是变量，见下一小节。

为什么说Python中的变量比其他语言强大的多呢？举个例子，`int8` 之所以是 `int8`，是因为它的底层只有8个位，如果学过计算机组成
就知道，计算机里所有的东西，它的底层都是0或者1来表示的。一个0或者1就是一个位，英文是 `bit`。而 `int8` 只有8个bit，也就是说，
它最多只能表示 `2 ** 8 = 256` 个状态，或者说数字。那么超过这个表示范围的怎么办呢？答案是使用更多的bit来表示，例如 `int16`。

而Python里可不用这样，Python自动帮我们处理好了底层的一切，你看，无论是1，还是 99999999999999999999999999999999999999999，
他们的类型都是 `int`：

```python
$ python
>>> type(99999999999999999999999999999999999999999)
<class 'int'>
>>> type(1)
<class 'int'>
```

这样子我们写代码的时候就方便很多，因为我们可以专注于我们真正要解决的问题，而不用管底层到底该用多少个bit来存储了😄。

## 变量

变量，顾名思义，它的值是可以变化的。变量名，就是一个名字，它代表着一个变量，比如 `a = 1`，a就是变量名，a在计算机内存里的
真正内容就是变量。不过实际上我们一般都会把 `a` 叫做变量 `a`，而不会严格去区分这两者的区别。举个例子，下面例子中的 `a` 就是个变量，
因为它的值一直在变化：

```python
$ python
>>> a = None
>>> a = 1
>>> a = 2
>>> a = "Hello"
>>> a = 1.234
>>> a = None
```

---

- 上一篇：[Hello World!](./hello_world.md)
- 下一篇：[容器类型](./composite_types.md)
