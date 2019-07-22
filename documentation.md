# Developer Notes

## Manager

### Functions
* load_vault()
<br>&nbsp;&nbsp;&nbsp;&nbsp;
This will load the vault at the current "path". Change path with set_path()<br><br>
* save_vault()
<br>&nbsp;&nbsp;&nbsp;&nbsp;
This will save the vault to the current "path". Change path with set_path(). It will create a new vault if none exists.<br><br>
* create_entry(title, username, password)
<br>&nbsp;&nbsp;&nbsp;&nbsp;
Creates an entry in the password manager. Example args: ("Ebay", "Email@gmail.com", "thepassword")<br><br>
* edit_entry(title, username="", password="")
<br>&nbsp;&nbsp;&nbsp;&nbsp;
Edit the entry "Title", with whatever args are given. Args left blank will remain unchanged.<br><br>
* delete_entry(title)
<br>&nbsp;&nbsp;&nbsp;&nbsp;
Delete the the entry "Title".<br><br>
* get_all_entries()
<br>&nbsp;&nbsp;&nbsp;&nbsp;
This will return all of the entries within the vault.<br><br>
* set_path(path)
<br>&nbsp;&nbsp;&nbsp;&nbsp;
Set the path to the current working file. 

### To Do
* When adding a new entry, check if entry "title" already exists.
* When loading vault from disk, ask user if they want to merge currently loaded entries or discard (in the case that the user has created entries with no vault loaded).
* AES-256 Encryption/Decryption with master key.
* More graceful handling of path.
