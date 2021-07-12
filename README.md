# Kid Keeper
A tool for keep your baby and kid! Or use for control system 🥺

## Demo
![Demo](./KidKeeperDemo.mp4)
- Or see `KidKeeperDemo.mp4` in main folder

## Screenshot
![screenshot](./root.png)

## installation
- Fisrt clone the repo:
```
$ git clone https://github.com/sina-yeganeh/kid-keeper.git
```

Then, setup the project using the installer script `installer.py`
```
$ python3 installer.py
```

Now you are ready to go!

## Running the application
You should run `kidkeeper.py` file to run the application:
```bash
$ python3 kidkeeper.py [-s or --screenshots]:int [-d or --delay]:float [--cliapp]:bool
```

### Example
```bash
$ python3 kidkeeper.py -s 5 -d 10
// takes 5 screenshots totally with 10 seconds of delay in between

$ python3 kidkeeper.py --screenshots 5 --delay 10
// exactly the same as the one mentioned above (using the full name of arguments)

$ python3 kidkeeper.py --cliapp
// starts the cli interface. if you specify this option you can not provide arguments anymore because it will override them all
```
## Command line arguments

- `-s` or `--screenshots`: specifies number of screenshots to take
- `-d` or `--delay`: specifies the delay between each screenshot
- `--cliapp`: starts the cli app interface if it is provided