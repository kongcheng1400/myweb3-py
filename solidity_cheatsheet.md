# 变量.
- 初始值为0.
## 数值类型(value type): 
  - bool
  - int, uint, uint256
  - address: 20bytes. 有成员变量.
    - payable
  - string:
## 引用类型(reference type): 数组和结构体.
  - bytes
    - 定长, 数值类型: byte, bytes1, bytes8, bytes32
    - 不定长，引用类型.
### 数组
- 固定长度: uint[8], bytes1[5]
- 可变长度. bytes, uint[], bytes1[]
- 对于memory修饰的动态数组，可以用new来创建，但是必须声明长度，而且长度不能改变. uint[] memory array8 = new uint[](5);
- 数组字面量: [uint(1), 2, 3], solidity如果一个值没有制定type, 默认就是最小该单位的type. 这时候就是uint8

### 结构体
struct Student{
    uint256 id;
    uint256 socre;
}
Student student;



#### 数组成员
- length
  
## 枚举enum
  
## 映射类型: Solidity中的哈希表.
- 声明映射: mapping(_KeyType => _ValueTYpe): mapping(uint => address) public idToAddress
### 规则
- _keytype只能选择默认类型: uint, address, 不能用自定义结构体. _ValueTYpe:可以使用自定义的类型.
- 映射的存储位置必须是storage.
- 如果映射为public, 那么solidity会自动给你创建一个getter函数，可以通过Key来查询对应的Value.
- 新增: _Var[_Key] = _Value

### 原理
- 映射不储存任何key的资讯，也没有length
- 映射使用keccak256
- Ethereum会定义所有未使用的空间为0, 所以未赋值Value的初始值为0.

## 函数类型:
  - function <function name> (<parameter types>) {internal|external|public|private} [pure|view|payable] [returns (<return types>)]
    - internal, external, public, private: 可见性
      - external: 只能合约外部访问(可以用this.f()来调用)
    - pure, view, payable: 权限
      - payable:带着它的函数，运行的时候可以给合约转入ETH.
    - returns/return
      - 多个返回值
      - 命名式返回.
  
## 表达式
  - 解构赋值
### storage/memory/calldata
- 引用类型包括数组array, 结构体struct, 映射: mapping. 赋值时直接传递地址.由于这类变量比较复杂，占用空间大，使用时必须声明数据存储位置:
- storage:存在链上，合约里的状态变量默认storage
- memory: 函数里的参数和临时变量: 存内存.
- calldata: 和memory类似， 不能修改

7. 变量的作用域
状态变量(state variable)， 局部变量， 全局变量.

状态变量
- 数据存储在链上，所有合约内的函数都可以访问. (合约内，函数外)

全局变量:
- solidity预留关键字，它们可以在函数内不声明直接使用:
- msg.sender, block.number, msg.data,

#### 全局变量-以太单位与时间单位.

solidity中不存在小数点， 以0代题为小数点， 利用以太单位可以避免误算的问题.
wei, gwei, ether.

时间单位:
seconds: 1
minutes: 60 seconds = 60
hours: 60 minutes = 3600
days: 24hours = 86400



## constant和immutable
- 只有数值变量可以声明constant和immutable; string和bytes可以声明为constant, 但不能为immutable.
- constant变量必须在声明的时候初始化，之后则不能改变.
- immutable变量可以在声明时或构造函数中初始化，因此更加灵活.

## control
- if else if else
- for
- while
- do-while
- ?: 三元

## 构造函数和修饰器
合约控制权限.
### 构造函数
- 部署合约的时候自动运行一次。
- 此时初始化合约的owner地址

#### 修饰器modifer
声明函数拥有的特性，并减少代码冗余， 让函数具有某些特定的行为.
- 使用场景：运行函数前的检查，例如地址，变量，余额等.


## 事件
两个特点:
- 响应
- 经济.
### EVM log
包含topics, 数据data.


## 继承
把合约看作是对象，solidity也是面向对象的编程，支持继承.
- virtual: 父合约中的函数，如果希望子合约重写，需要加上virtual关键字.
- override: 子合约重写了父合约中的函数，需要加上override关键字.
- 用override修饰的

### 多重继承
1. 继承时按照最高到最低: contract Erzi is Yeye, Baba;
2. 如果某一个函数在多个继承的合约里都存在， 比如例子中的hip(), pop(), 在子合约里面必须重写，不然会报错.
3. 重写在多个父合约中都重名的函数时，override关键字后面要加上所有父亲的名字，例如override(Yeye, Baba)

### 构造函数的继承
1. 在继承时声明父构造函数的参数，例如contract B is A(1)
2. 在子合约的构造函数中声明构造函数的参数.

### 抽象合约和接口
如果一个智能合约里至少有一个未实现的函数，则必须为abstract

#### 接口
类似于抽象合约但是不实现任何功能。接口的规则:
1. 不能包含状态变量
2. 不能包含构造函数
3. 不能继承接口外的其他合约
4. 所有函数都必须是external且不能有函数题
5. 继承接口的合约必须实现接口定义的所有功能.

如果智能合约实现了某种接口(ERC20/ERC721)，其他Dapps和智能合约就知道如何与它交互。因为接口提供了两个重要信息:
1. 合约里每个函数的bytes4选择器，以及函数签名:函数名(每个参数类型.)

### 异常: error, require, assert
- error 0.8.4版本新加的内容，方便且高效的向用户解释操作失败的原因. error必须搭配revert使用.
- require: 0.8之前抛出异常的方法: gas随着描述异常的字符串的长度增加，比error命令要高。使用方法 require(检查条件， "异常的描述")
- assert: 不知道异常信息.



## 库合约
库函数是一种特殊的合约，为了提升solidity 代码的复用性和减少gas而存在。库合约一般都是一些好用的函数合集(库函数)
1. 不能存在状态变量
2. 不能够继承或者被继承.
3. 不能接收以太币.
4. 不可以被销毁.

### 使用
using for 指令: using A for B;
或者通过库合约名屌用库函数.
String: 将uint256转换为String
Address: 判断某个地址是否为合约地址
Create2:更安全的使用Create2 EVM opcode
Arrays: 跟数组相关的库函数.

## import
利用import导入其他合约中的全局符号(外部源代码)

## 接收 ETH recieve和fallback
0.6.4版本之前，只有fallback()函数。0.6之后solidity才将fallback()函数拆分成receive()和fallback()两个函数.
solidity支持两种特殊的回调函数: receive()和fallback().
1. 接收ETH
2. 处理合约中不存在的函数调用.(代理合约 proxy contract)

### recieve
只用于处理接收ETH.
- 一个合约最多只有一个receive()函数，声明方式与一般函数不一样，不需要function关键字:
- recieve() external payable {...} 不能有参数，不能有返回值，必须包含external和payable

### fallback
在屌用合约不存在的函数时被触发。可用于接收ETH,
- 必须由external 

## send ETH
transfer(), send(), call() 其中call()是被鼓励的用法.
