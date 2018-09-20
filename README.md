# Personnal i3 configuration

## Install
```bash
# Clone
mkdir -p ~/.config/i3
cd ~/.config/i3
git clone https://github.com/caymard/i3-config .

# Python venv
mkdir -p ~/.venvs/i3
virtualenv -p python3 ~/.venvs/i3
source ~/.venvs/i3/bin/activate
pip install -Ur requirements.txt
deactivate

# Wake lock service
sudo cp services/wakelock.service /etc/systemd/system/
sudo systemctl daemon-reload
```

## Configuration
```bash
cd scripts
cp local_settings.py.example local_settings.py
# then fill the tokens/API keys.
```
