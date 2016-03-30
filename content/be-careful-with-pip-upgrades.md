Title: Be careful with PIP upgrades!
Date: 2016-03-30 23:59
Category: python
Tags: python, pip, upgrades

Hey guys! How are you going?
It have been a long time since my last post, I was working a lot and I had no time to read more, sorry...

On this post I will talk about an experience that my friend and I lived upgrading PIP packages.

#### The situation
The Magazine Luiza's website was writted with Bottle, and is a bit old, so, as you can imagine, the PIP package's versions are old too.
We use Jinja2 to render templates, and, we wanted to upgrade some packages just to feel more confortable.
Well, we saw on `requirements` that Jinja2 was on version `2.5.5` and the last version was `2.8`, so, we just changed the `2.5.5` to `2.8` and installed the requirements again. _Easy, huh?_

But we didn't expect that this would broke almost everything! But, why?

#### The error
At some templates files, Jinja was throwing the error: `non-default argument follows default argument`, but, wtf? We just upgraded to the new version! What's wrong? What have changed?

We are almost getting crazy when we decided to search on Google, and, we saw this on [Jinja2's Version 2.8 Changelog](http://jinja.pocoo.org/docs/dev/changelog/#version-2-8):
```
* Added a check for default arguments followed by non-default arguments. This change makes {% macro m(x, y=1, z) %}...{% endmacro %} a syntax error. The previous behavior for this code was broken anyway (resulting in the default value being applied to y).
```

#### Okay, but, what's wrong?
You must be thinking: `My gosh, this is stupid, everyone knows the default arguments are always first!`.

Yeah, but, like I said, the code is old, and Jinja didn't had this check before, and we have found a lot of `macros` like that:
```
{% macro test(a, b, c=None, d) -%}
	bla bla bla
{%- endmacro  %}
```

So, we had to refactor every piece of code that have this error... <sad>

#### What to learn with that?
Be careful when upgrading PIP packages, test everything after that, i said EVERYTHING.

And, when you install some package, try to put the version in the `requirements` file, like:
```
Jinja2==2.8
```

If you just put `Jinja2` you will always get the last version, but, a simple upgrade can broke your project.

> Tip of the day: A no noticeable error can f*ck everything!

That's all, cya!
