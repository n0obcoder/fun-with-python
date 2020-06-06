<h1>todo_list_maker</h1>

This is a simple todo_list_maker application that I have built in Python.

<h2>Running the todo_list_maker to add a new todo list item to the default todo list(.txt file) at the default location (Desktop)</h2>

```
python todo_list_maker.py --do "Learn Ableton Live 10"
```

<h2>Running the todo_list_maker to add a new todo list item to the specified todo list(todo_music.txt for this example) at the default location (Desktop)</h2>

```
python todo_list_maker.py --do "Learn Ableton Live 10" --name "todo_music"
```

<h2>Running the todo_list_maker to add a new todo list item to the specified todo list(todo_music.txt for this example) at the specified location (C:/Users/anime/Documets/)</h2>

```
python todo_list_maker.py --do "Learn Ableton Live 10" --name "todo_music" --path "C:/Users/anime/Documets/"
```

<h2>Running the todo_list_maker to add a new todo list item by renewing the todo list(if it exists already)</h2>

```
python todo_list_maker.py --do "Learn Ableton Live 10" -n
```

<h2>Listing (printing) down all the to-do list items of the to-do list on the command-line</h2>

```
python todo_list_maker.py -l
```











<h2>Calling the API</h2>

```
python call_my_api.py
```

There are a variety of different URLs listed in call_my_api.py which can be hit using the API.

