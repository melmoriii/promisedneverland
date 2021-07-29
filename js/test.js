let password = '';
let rightPassword = 'qwerty';
while (password != rightPassword){
	password = prompt('Введите пароль:', '');
	if (password == null){
		break;
	}
}