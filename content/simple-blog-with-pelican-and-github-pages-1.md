Title: Create a simple blog with Python Pelican and Github Pages - Part One
Date: 2016-01-18 23:59
Category: python
Tags: python, pelican, github

Hello!<br/>
For the first post of my blog, why not talk about how to create one blog like this?<br/>
I will teach you how to create a simple blog using Pelican and host on Github Pages.<br/>
I'm gonna break this tutorial in **two parts**, this first part i will teach how to create your blog and at the second part i will teach how to host on Github Pages. Let's start!

# What's Pelican?
*"Pelican is a static site generator, written in Python, that requires no database or server-side logic."* [From Pelican's website](http://blog.getpelican.com/).

# What's the logic?
You just need to write `markdown` files and this will be your pages and/or posts.<br/> Pelican will do all the magic :)

# Cool! How do i start?

So, first of all, you need to ensure that you have [python](https://www.python.org "How to install Python"), [pip](https://pip.pypa.io/en/stable/installing/ "How to install Pip") and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org "How to install Virtualenvwrapper").

Let's assume that you already installed everything.

First of all, let's create the blog directory and go to folder:
```
$ mkdir blog && cd blog
```

Now you're on blog directory, let's create the virtualenv with virtualenvwrapper:
```
$ mkvirtualenv blog
```

Okay, you are now in virtualenv `blog`, let's install **pelican** using pip:
```
(blog) $ pip install pelican markdown
```

Now you have **pelican**, to start your blog project just run:
```
(blog) $ pelican-quickstart
```

This command will ask you some questions about your blog and after that it will generate the basic files of your blog.

**My recommended answers to start:**
```
> Where do you want to create your new web site? [.] <just press Enter>
> What will be the title of this web site? <Title of your blog>
> Who will be the author of this web site? <Your name>
> What will be the default language of this web site? [en] <just press Enter>
> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) n
> Do you want to enable article pagination? (Y/n) y
> How many articles per page do you want? [10] <just press Enter>
> What is your time zone? [Europe/Paris] <Your timezone> --> Check help below <--
> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) y
> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) y
> Do you want to upload your website using FTP? (y/N) n
> Do you want to upload your website using SSH? (y/N) n
> Do you want to upload your website using Dropbox? (y/N) n
> Do you want to upload your website using S3? (y/N) n
> Do you want to upload your website using Rackspace Cloud Files? (y/N) n
> Do you want to upload your website using GitHub Pages? (y/N) y
> Is this your personal page (username.github.io)? (y/N) y
```
> **Don't know your timezone? Maybe this [link](http://php.net/manual/en/timezones.php) will help you.** (I know it's `PHP`, but it will really help :P)


## The cool part, writing posts

Now you can check that you have a folder called `content`, right?<br/>
This folder is where your content must be.<br/>
Let's start creating a simple hello world.<br/>

Go to `content` folder:
```
(blog) $ cd content
```

Create a file called `hello.md`:
```
(blog) $ touch hello.md
```

Okay, now, open this file with you preferred text editor, i'll open with `vim`:
```
(blog) $ vim hello.md
```

And copy/paste this into `hello.md`:
```
Title: My hello world
Date: 2016-01-18 23:59
Category: Curious

Hey, this is my awesome hello world!
```

Every markdown file here need to have a minimal header as you can see above.<br/>
You need to have at least `Title`, `Date` and `Category`.<br/>
Everything you write after the header will be the post content.

## Nice, i feel's like a writer but how to make it work now?

This is the most simple part, after write your post(s), you just need to:

If you are on `content` folder, first you need go back to root folder:
```
(blog) $ cd ..
```

Then run:

```
(blog) $ pelican content
```

You'll see a message like:<br/>
`Done: Processed 1 articles, 0 drafts, 0 pages and 0 hidden pages in 0.25 seconds.`

This command will take every markdown file under `content` folder and generate the `html` pages on `output` folder.

*Easy, huh?*

## That's awesome, but, i'm not ready to push yet, how can i check it locally?

To run your blog locally simple run:
```
(blog) $ make serve
```

And go check your awesome blog in: [http://localhost:8000](http://localhost:8000)

Now you have a really nice blog running locally!
On the next post i will teach how to host it on Github Pages.

# Tips:

If you don't want to run `pelican content` everytime you change a markdown file, you can run (*from root folder*):
```
(blog) $ make regenerate
```

This command will start a `real-time monitor` that checks if some `content`, `theme` or `settings` was changed, then runs `pelican content` automatically!


Another cool tip is, if you are in development environment and want to serve your blog and check content in background automatically, you can run:
```
(blog) $ make devserver
```

This will act like if you are running `make serve` and `make regenerate` together, but in **background**! Awesome!
If you want to stop the `devserver`, just run:
```
(blog) $ make stopserver
```

And the `devserver` will be stopped!

**Damn!** This Pelican is really awesome!

That's all for today, cya!