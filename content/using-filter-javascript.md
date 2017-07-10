Title: Using filter() in Javascript
Summary: Learn how to easily filter Arrays using the Array.prototype.filter method!
Date: 2017-07-09 23:38
Image: js-logo.png
Category: javascript
Tags: javascript, functional programming

Hey, what's up?!

Today I want to teach you guys how to easily filter **Arrays** using the <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter" target="_blank">Array.prototype.filter</a> method.

The **filter()** method it's very simple to implement but it's also very powerful and helpful way to filter your data.

In this article, I'll use the same example data object that I used on my previous article, about the <a title="Check my last article about map() in javascript" href="http://guilhermetoti.com/2017/07/07/using-map-in-javascript/" target="_blank">map()</a> method.

So, the example data object is:
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
<br/>Let's imagine that you want to get from this array, only the objects where the **location.state** are equal to **SP**.

Maybe on a first approach, you might be thinking on something like:
```
let newData = [];

for (let index in data) {
  const currentElement = data[index];
  if (currentElement.location.state === 'SP') {
    newData.push(currentElement);
  }
}
```
<br/>It would work, right? Right, but, we are creating another variable to handle the new data and looping through the **data** object, searching for a state equal to **SP** and then, pushing this object to the new variable.

I think we can do better than this, dont we?

**Yes! We can do it better!** Using the **filter()** method!

Let's see how it would be written using the **filter()** method:
```
const newData = data.filter(function(currentElement) {
  return currentElement.location.state === 'SP';
});
```
<br/>The basic idea of the **filter()** method is:
```
- Pass to the filter() method a function who:
  - Receives the current element of the data array you're filtering;
  - Do your logic;
  - Returns a boolean;
- The filter() method will loop through the data array executing your function and passing each element of the array as a param;
- If your function has returned true, then the current element will be added to the new array;
- Otherwise it will be just ignored;
- Returns the new array with the filtered data;
```
<br/>And if you are learning about **ES6**, the same code could be written as:
```
const newData = data.filter((currentElement) => currentElement.location.state === 'SP');
```
<br/>Cool, huh? :D
<br/> You can see the **JSFiddle** of this article <a href="https://jsfiddle.net/guilhermetoti/ab4gpvvt/" target="_blank">here</a>.

Problably at this moment you must be thinking about your old codes and how to refactor them to use the **filter()** method, right?

Well, I hope so!

That's it! If you guys have some question, please comment below!
