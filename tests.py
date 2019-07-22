import manager


def main():

	subject = manager.manager()

	test_load_vault(subject)

	test_create(subject)
	
	test_edit(subject)

	test_delete(subject)


	test_save(subject)



'''Create a new vault with 1 entry'''
def test_create(manager):

	manager.create_entry("Ebay", "sockpuppet@tinymail.com", "abracaknobra123")
	manager.create_entry("Amazon", "testywesty@gmail.com", "unifiedLlamaAliance")
	manager.create_entry("Leetcode", "l33thaxor@overengineering.com", "look@myhax")
	manager.create_entry("Youtube", "sockpuppet@tinymail.com", "abracayoutubera123")
	manager.create_entry("github", "testPractitioner@hubofthegit.net", "shoenice22")

	'''Should ask the user to overwrite'''
	manager.create_entry("Ebay", "sockpuppet@tinymail.com", "asdknfasndfnsd")


	print(manager.get_all_entries())



'''Edit existing vault'''
def test_edit(manager):


	manager.edit_entry("Youtube", "Turbosqueeze@donkeyfoot.com", "jdshjfbakjhsdf")
	manager.edit_entry("Leetcode", password="ATESTLEETPASSWORD")


	print(manager.get_all_entries())


def test_delete(manager):
	
	manager.delete_entry("Amazon")
	manager.delete_entry("Steam")

	print(manager.get_all_entries())


def test_save(manager):

	print('\n\nSAVING VAULT.....')
	manager.save_vault('.\\vault.json')
	print('\nVAULT SAVED!\n\n\n')


'''Should say that none exists, "create now?" '''
def test_load_invalid():
	pass


def test_load_vault(manager):
	print('\n\nLOADING VAULT\n')
	manager.load_vault(".\\vault.json")
	print('\nVAULT LOADED!\n\n\n')

'''Test creating entries, then loading a vault. Upon closing
the vault, it should ask if you want the rogues merged in'''
def test_rogueEntries():
	pass


if __name__ == '__main__':

	main()