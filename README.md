# mite_server_app

<b>Часть моего проекта "MITE" - Make IT Easy.</b>

Создание WEB-интерфейса на Flask для выполнения несложных задач в Ansible.

В этом примере показано как Системным Администратор может предоставить пользователю возможность самостоятельно устанавливать/удалять программы на ПК, при этом не выдавая ему права Администратора.<br> Через WEB-интерфейс пользователь подает "Заявку". Flask передает в Ansible два параметра IP-клиента и какой playbook надо выполнить. Ansible подключается к ПК сотрудника и выполняет необходимые действия. Все программы будут устанавливаться через Chocolatey package manager т.е. плюс в том что не нужно создавать файловое хранилище для инсталляционных пакетов, а минус в том что это Chocolatey а значит гарантировать доступность пакетов невозможно... 

# Как установить

* Клонируем репу на Linux сервер.
* Разворачиваем виртуальное окружение через virtualenv
* Устанавливаем все необходимые зависимости с файла <b>requirements.txt</b> <i>(В зависимости так же добавлены модули работы с Kerberose для работы в AD)</i>.
* В корне проекта необходимо создать файл <b>conf.txt</b><br>

<b>С вот таким содержимым в случае если вы используете для подключения локального администратора</b>:<br>
[all:vars]<br>
ansible_ssh_user=<admin_login><br>
ansible_ssh_pass=<admin_password><br>
ansible_ssh_port=5986<br>
ansible_connection=winrm<br>
ansible_winrm_server_cert_validation=ignore<br>


<b>Или если вы находитесь в домене ваш файл будет примерно такого вида</b>:<br>
[all:vars]<br>
ansible_winrm_transport=kerberos<br>
ansible_ssh_user="admin_user@YOU.DOMAIN.TLD"<br>
ansible_ssh_pass=<admin_pass><br>
ansible_ssh_port=5986<br>
ansible_connection=winrm<br>
ansible_winrm_server_cert_validation=ignore<br>
ansible_winrm_scheme=https<br>
ansible_winrm_kerberos_delegation=true<br>

Так же в случае с AD вам пройдётся установить kubectl и прописать в /etc/krb5.conf данные по своему домену.

* Последнее что необходимо сделать, выполнить вот этот скрипт на всех Windows ПК к которым хотите предоставить доступ для Ansible.
https://github.com/ansible/ansible/blob/devel/examples/scripts/ConfigureRemotingForAnsible.ps1

Это только протопит. В скором времени выложу Docker-контейнер для удобства развертывания...
