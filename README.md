Podsumowanie trzech komend które wykonałeś

python -m venv .venv — stworzyło folder .venv z własną kopią Pythona i pip. To operacja jednorazowa na początku projektu.

.venv\Scripts\activate — "przełączyło" terminal żeby używał Pythona z .venv. To robisz za każdym razem gdy siadasz do pracy nad projektem. Gdy zamkniesz terminal, aktywacja znika — przy następnej sesji musisz aktywować ponownie.

pip install -r requirements.txt — zainstalowało wszystkie biblioteki do .venv\Lib\site-packages\, nie globalnie. Gdybyś uruchomił to samo bez aktywowanego venv, biblioteki wylądowałyby w globalnym Pythonie i cały sens izolacji by przepadł.

Jedna praktyczna rzecz do zapamiętania
Za każdym razem gdy otwierasz projekt w nowej sesji terminala:
powershell# You will need to do this every time you open a new terminal
.venv\Scripts\activate

# You should see (.venv) — only then run python or pip
(.venv) PS C:\Users\konra\Projects\smart-parking-ml>