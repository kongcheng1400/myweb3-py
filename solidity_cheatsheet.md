# 变量.
- 初始值为0.
## 数值类型(value type): 
  - bool
  - int, uint, uint256
  - address: 20bytes. 有成员变量.
    - payable
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