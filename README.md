ansible-galaxy collection install vyos.vyos

ansible-galaxy collection install netbox.netbox


ansible-playbook -i inventory.yml playbook.yml --limit RTR-ALTSTADT -k

ansible-playbook -i inventory.yml playbook.yml --check --diff

ansible-playbook -i inventory.yml playbook.yml

ansible-playbook -i inventory-central.yml playbook-central.yml -k