Title: Using map() in Javascript
Summary: Learn how to use this simple and powerful javascript function called .map with easy and real-life examples.
Date: 2017-07-07 15:31
Category: javascript
Tags: javascript, functional programming

Hello guys, how're you doing?
Hope you're doing great!

In this post, I want to talk about the **<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map" target="_blank">map()</a>** function, a function related to `Arrays` in Javascript that I use a lot and it's very useful for various situations.

I'll show you guys some real-life examples, hope you guys like it!

#### map()
The **map()** function is very useful when you need to translate or change the elements in an Array.
<br/>It loops through the Array **from left to right**, creating a new Array, and, for each item, it runs some function that you passed as args, and your function must return an value, so, this return will be the new item of the new Array.

<br/>Let's see an example below.

<br/>Imagine that you receive this data from your API:
```
const data = [
  {
    id: 1,
    name: 'John Doe',
    location: {
      city: 'São Paulo',
      state: 'SP',
      country: 'Brazil',
      zipcode: '00000-000'
    }
  },
  {
    id: 2,
    name: 'Doe John',
    location: {
      city: 'Rio de Janeiro',
      state: 'RJ',
      country: 'Brazil',
      zipcode: '11111-111'
    }
  },
  {
    id: 3,
    name: 'Joe Dohn',
    location: {
      city: 'Curitiba',
      state: 'SP',
      country: 'Brazil',
      zipcode: '123456-789'
    }
  }
]
```
So, you have an array of objects with:
```
- user id
- name
- location
```
Let's figure out we don't need all this data, we need only an array with objects like:
```
{
  id: 1,
  name: 'John Doe',
  city: 'São Paulo'
}
```
Problably, to resolve that, you may be thinking in something like:
```
let newData = [];

for (var index in data) {
  const user = data[index];
  
  newData.push({
    id: user.id,
    name: user.name,
    city: user.location.city
  })
};
```
Right?
<br/>It isn't wrong, and it's works, but, there is a lot of steps, and, we can do it better!
<br/>Doing that way, you are:
```
1. Instancing a new variable;
2. Doing a `for` loop through the `data` Array, getting each index`;
3. Using this `index` to access the current element of the Array;
4. Pushing the new object to the variable previously created;
```
The **map()** function provides an easy way to do exactly this and with less steps!
<br/>Check below how to write the same using **map()**:

```
const newData = data.map(function(item) {
  return {
    id: item.id,
    name: item.name,
    city: item.location.city
  }
});
```
Maybe your reaction be like:
![WTF]({filename}/images/wtf.gif)

<br/>But, keep calm, i'll explain every step!
<br/>When you execute **Array.map()**, to clear your mind in a _real-life_ example, you can think in something like:
```
1. The map() gets your Array;
2. Loop through it, and, for each item it:
   1. Execute the function you've passed, passing the current item as an argument;
   2. Update the current item value, to the returned value from your function;
```
So, this also can be re-written to something like:

```
function parseItem(item) {
  return {
    id: item.id,
    name: item.name,
    city: item.location.city
  }
}

const newData = data.map(parseItem);
```
It will produce the same result and has the same effect.

And if you're familiar with ES6, you can re-write it to:
```
const newData = data.map(({ id, name, location: { city } }) => ({ id, name, city }));
```
But i'll not talk about ES6 now, maybe in another post! :P
<br/><br/>Using any of the examples above, if you run a **console.log(newData)**, you will receive:

```
[
  {
    "id": 1,
    "name": "John Doe",
    "city": "São Paulo"
  },
  {
    "id": 2,
    "name": "Doe John",
    "city": "Rio de Janeiro"
  },
  {
    "id": 3,
    "name": "Joe Dohn",
    "city":"Curitiba"
  }
]
```
So, that's it guys, as expected!!
<br/>You can see the **JSFiddle** of this post <a href="https://jsfiddle.net/guilhermetoti/bju032cw/" target="_blank">here</a>
<br/><br/>I hope you guys understand about the **map()** function, but, if you have any questions please comment below!
