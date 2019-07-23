# <b><u>Developer Notes - Manager</u></b>


## Functions
* load_vault()
<br>&emsp;
This will load the vault at the current "path". Change path with set_path()<br><br>


* save_vault(merge=True)
<br>&emsp;
This will save the vault to the current "path". Change path with set_path(). It will create a new vault if none exists. If merge is True, the loose_entries will be saved into the vault<br><br>

* close_vault(save=True)
<br>&emsp;
Closes the currently opened vault. If save is True, it will save the current vault with default save_vault() parameters.<br><br>


* create_entry(title, username, password)
<br>&emsp;
Creates an entry in the password manager.
<br>&emsp;
Example args: ("Ebay", "Email@gmail.com", "thepassword")
<br><br>


* edit_entry(title, username="", password="")
<br>&emsp;
Edit the entry "title", with whatever args are given. Args left blank will remain unchanged.<br><br>


* delete_entry(title)
<br>&emsp;
Delete the the entry "title".<br><br>


* get_all_entries()
<br>&emsp;
This will return all of the entries within the vault.<br><br>

* get_entry(title)
<br>&emsp;
Return the entry titled "title".<br><br>

* set_path(path)
<br>&emsp;
Set the path to the current working file. <br><br>

---
## Notes

<br><br>
In the interest of keeping things SOLID, the manager will not generate a password if none is provided (to keep it as purely an entry manager only). If the user provides no password when creating an entry, the password generation should be called from the CLI and its result passed to create_entry as an argument.
<br><br>

### Loose Entries
If the user should create entries with no vault loaded they will get added to the entries dictionary. If then the user loads a vault into "entries", the previous entries will be moved to a new dictionary called "loose entries". These are entries that currently exist in the current session but are not part of the vault. Call save_vault(merge=True) to merge the loose entries into the currently opened vault.
<br><br>

### To Do
* AES-256 Encryption/Decryption with master key.
* More graceful handling of path.
* Add username or ID to vault rather than generic vault.json to prevent accidental overwriting of other vaults.

