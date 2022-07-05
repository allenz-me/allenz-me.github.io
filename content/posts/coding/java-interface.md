---
title: "Java常用接口类的方法简介"
date: 2020-02-26
draft: false
slug: java-interface
categories: ["算法与程序设计"]
tags: ["Java"]
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---



<img src="../../figures/java-interface/v2-2f459861d963c59dddd56d7466da4381_1440w.jpg" alt="" style="zoom: 80%;" />



`Collection` 是 Java 中许多内置类的基类，它是存储“一堆”对象 `object` 的容器最抽象的表示；`Collection` 接口 继承自 `Iterable` 接口 ，提供了序列对象最基本的方法。

```java
public interface Collection<E> extends Iterable<E> {
    int size();
    boolean isEmpty();
    boolean contains(Object o);
    Iterator<E> iterator();
    Object[] toArray();
    <T> T[] toArray(T[] a);
    boolean add(E e);
    boolean remove(Object o);
    boolean containsAll(Collection<?> c);
    boolean addAll(Collection<? extends E> c);
    boolean removeAll(Collection<?> c);
    boolean retainAll(Collection<?> c);
    void clear();
    boolean equals(Object o);
    int hashCode();
}
```

中间返回 `boolean` 类型的添加/删除操作，当改变这个序列的时候返回 `true`，没有改变则返回`false`。

另外 `Collection` 接口还有几个用 `default` 关键字修饰的方法，这里不提。

诸如 `Stack`、`ArrayList`、`HashSet` 等类都实现了 `Collection` 接口，因此这些类在使用的时候可以直接调用 `Collection` 定义的接口方法。

`AbstactCollection` 是一个实现 `Collection` 的抽象类，基于 `add` 方法我们可以很容易地补全 `addAll` 方法，有 `remove` 方法那么 `removeAll` 也就呼之欲出了，`AbstractCollection` 正是做了这样一件事情。

### 线性表 `List`

`List` 接口继承自 `Collection` 接口，除去 `Collection` 定义的基本方法以外，还定义了线性表的几种基本操作：

```java
public interface List<E> extends Collection<E> {
    E get(int index);
    E set(int index, E element);    // return the element previously at the specified position
    void add(int index, E element);
    E remove(int index);
    int indexOf(Object o);
    int lastIndexOf(Object o);
    List<E> subList(int fromIndex, int toIndex);
}
```

除此之外，还定义了一个 `default` 关键字修饰的 `void sort()` 方法，所以对于 `ArrayList` 和 `LinkedList` 对象，可以直接调用 `.sort()` 方法进行排序（可传入一个 `Comparator<E>`） 。

`AbstractList` 抽象类 类似于 `AbstractCollection`， 基于 `add`、`remove`、`Iterator` 实现了 `addAll`、`removeAll`、`toArray`、`indexOf` 等方法。

在Java中，`ArrayList `和 `LinkedList` 分别是线性表的 `顺序表` 和 `双链表`  实现。

`LinkedList` 除了是双链表以外，还有其他重要的功能。

**先看 `ArrayList`**，它的初始化方式有三种
1. 不接收参数
2. 传入一个整数表示初始容器的容量
3. 传入一个 `Collection` 对象进行拷贝（调用该对象的迭代器将各元素依次拷贝放入 `List` 中）

```java
public class ArrayList<E> extends AbstractList<E>
        implements List<E>, RandomAccess, Cloneable, java.io.Serializable {
    public ArrayList(int initialCapacity)    // 初始容量
    public ArrayList()
    public ArrayList(Collection<? extends E> c)    // 拷贝别的容器
}
```

**小tips: 可以用第三种初始化方法返回列表的浅拷贝哦。**

**另外，从 `Array` 创建 `ArrayList` 可以这样子：**

```java
ArrayList<Integer> l = new ArrayList<>(Arrays.asList(1, 2, 3));
ArrayList<String> l = new ArrayList<>(Arrays.asList("a", "b", "c"));
// Arrays.asList(new int[]{1, 2, 3}); 这样是不可以滴
```

`ArrayList` 内部维护了一个数组 `elementData`，每当容量达到上限时便进行扩容。

同时，要注意，`ArrayList` 是**线程不安全**的 。

### 栈 `Stack`

`Stack` 类继承 `Vector` 类，是一个线程安全的栈的实现。`Vector` 类现在已经很少用到了。

```java
public class Stack<E> extends Vector<E> {
    public Stack() {}
    public E push(E item)
    public synchronized E pop()
    public synchronized E peek()
    public boolean empty()
    public synchronized int search(Object o)
}
```

官方建议如果有使用栈的需求的时候，可以实现了 `Deque` 接口的 `ArrayDeque` 作替代，因为 `ArrayDeque` 能提供更多的功能。

### 队列 `Queue`

注意，**`Stack` 是一个类而 `Queue` 只是一个接口**。它定义了

+ `offer` 入队
+ `poll` 出队
+ `peek` 访问队首

事实上，队列完全可以使用双端队列去替代，通常我们会使用 `LinkedList` 作为队列来使用。

```java
Queue<Integer> queue = new LinkedList<>();
```

### 双端队列 `Deque`

`Deque` 也是一个接口，在 Java 中有两个常用的实现类：`LinkedList`（基于双链表）和 `ArrayDeque`（基于循环数组）。

这两个实现类的数据结构不同，决定了它们的一些**差异**：

+ `LinkedList` **访问队列中间的元素**需要时间 $O(n)$ ，而 `ArrayDeque`只需要 $O(1)$
+  `ArrayDeque` 内部维护了一个固定大小的数组，所以在添加元素的时候可能需要**扩容**

先看 `Deque` 接口定义的通用操作：

```java
public interface Deque<E> extends Queue<E> {
    void addFirst(E e); void addLast(E e);
    boolean offerFirst(E e); boolean offerLast(E e);
    E removeFirst(); E removeLast();
    E pollFirst(); E pollLast();
    E getFirst(); E getLast();
    E peekFirst(); E peekLast();
    //  其它方法
}
```

乍一看 `add` 方法和 `offer` 方法作用相同、`remove` 方法和 `poll` 方法、`get` 和 `peek` 方法都很接近；它们之间的不同在于，用于 `Queue` 接口的函数名类型（如 `offer`、`peek` 等），在数据为空时不会报错（返回 `null`） 。

`Deque` 接口的方法加上 `List` 接口的方法，就基本组成了 `LinkedList` 的方法！

再看 `ArrayDeque`，其初始化方式类似于 `ArrayList`：

```java
public class ArrayDeque<E> extends AbstractCollection<E>
                           implements Deque<E>, Cloneable, Serializable
{
    public ArrayDeque();
    public ArrayDeque(int numElements); // 数组的初始容量，默认 16
    public ArrayDeque(Collection<? extends E> c);
}
```

然后是 `LinkedList`：

【未完待续】



### 优先队列 `PriorityQueue`

优先队列的底层数据结构是堆，堆其实是用数组表示的一棵完全二叉树。当元素数量增加的时候，用于表示堆的数组也是需要动态扩容的。

先看初始化方法，默认使用**小顶堆**：

```java
public class PriorityQueue<E> extends AbstractQueue<E> 
        implements java.io.Serializable {

    public PriorityQueue();
    public PriorityQueue(int initialCapacity);  // 不传入 Comparator 则会使用类的默认比较方法
    public PriorityQueue(Comparator<? super E> comparator);
    public PriorityQueue(int initialCapacity,
                         Comparator<? super E> comparator);
    public PriorityQueue(Collection<? extends E> c);
    public PriorityQueue(PriorityQueue<? extends E> c);
    public PriorityQueue(SortedSet<? extends E> c);
```

`PriorityQueue` 完全支持队列的接口操作。使用的关键在于传入的 `Comparator`，如果要使用最大堆的话，需要传入相应的 `Comparator`（可以使用Java 8的lambda表达式）

### 集合 `Set`

`Set` 接口继承了 `Collection` 接口，并没有添加什么特殊的方法；一切与 `Set` 相关的其它接口都直接或间接继承了 `Set` 接口。

`TreeSet` 是基于平衡二叉查找树的集合类型，而 `HashSet` 基于哈希表。还有一种可能听的少，叫做 `LinkedHashSet`。

`HashSet` 的底层其实是 `HashMap`，其初始化方式也跟 `HashMap` 非常的相似！

`TreeSet` 是一个非常重要的数据结构，顾名思义，要认识 `TreeSet`，必须先了解 Java 里面几个与集合紧密相关的几个接口！

先是 `SortedSet`，它实现了 `Set` 接口，内部有一个 `Comparator<E>`，提供以下几种常用方法：

```java
SortedSet<E> subSet(E fromElement, E toElement);  // 包含 fromElement, 不包含toElement
SortedSet<E> headSet(E toElement);  // 包含所有严格小于 toElement 的元素
SortedSet<E> tailSet(E fromElement);  // 包含所有大于等于 fromElement 的元素
E first();  E last();  // 返回最小、最大的元素
```

`NavigableSet` 是 `SortedSet` 的“升级版”！提供了更多与“比较”有关系的函数。

```java
E lower(E e);  // 返回最大的、严格小于 e 的元素，如果没有，返回 null
E floor(E e);  // 返回最大的、小于等于 e 的元素，如果没有，返回 null
E ceiling(E e);  // 返回最小的、大于等于 e 的元素，如果没有，返回 null
E higher(E e);  // 返回最小的、严格大于 e 的元素，如果没有，返回 null
E pollFirst();  // 删除并返回最小的元素 (first)
E pollLast();  // 删除并返回最大的元素 (last)
NavigableSet<E> descendingSet();  // 返回一个相反的 NavigableSet (相反的 Comparator<E>)
Iterator<E> descendingIterator();
NavigableSet<E> subSet(E fromElement, boolean fromInclusive,
                           E toElement,   boolean toInclusive);
NavigableSet<E> headSet(E toElement, boolean inclusive);
NavigableSet<E> tailSet(E fromElement, boolean inclusive);
// 以上的那几个函数与 SortedSet 的相关函数类似
```

`TreeSet` 的实现基于 `TreeMap`，有如下几种初始化方式：

```java
public class TreeSet<E> extends AbstractSet<E>
    implements NavigableSet<E>, Cloneable, java.io.Serializable
{
    public TreeSet();  // 使用自然顺序，插入的元素的超类必须实现 Comparable 接口
    public TreeSet(Comparator<? super E> comparator);
    public TreeSet(Collection<? extends E> c);
    public TreeSet(SortedSet<E> s);
}
```

`TreeSet` 的类方法大致就是 `NavigableSet` 和 `SortedSet` 的结合体。

`HashSet` 相对来说就没有那么多复制的操作了。默认的初始化容量是16，装填因子是0.75。



### 映射/字典 `Map`

`Map` 类型是 Java 中非常重要的类型，类似于 `Set`，`TreeMap` 使用基于**键**的平衡二叉查找树，而 `HashMap` 使用哈希表。`TreeMap`、`HashMap` 都实现了`AbstractMap` 抽象类，映射的实现，相当于 Python 中的 `dict` 字典类型。

```java
	V get(object key);
	containsKey(object key);
	V put(K key, V value);
	V remove(object key);
	containsValue(object v);
	keySet()
  values()
  getOrDefault(object key, V defaultValue)
  putIfAbsent(K key, V value)
  entrySet()
```



`HashMap` 的初始化方法有多种，常见的有这三种：
1. 无参数 
2. 整数（表示初始容量）
3. 整数，浮点数（表示初始容量和装填因子）



【未完待续】
