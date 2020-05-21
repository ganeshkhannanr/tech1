#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
           msg=dict(type='str')
        )
    )
    
    result = dict(
        output = module.params['msg'],
        changed=False
    )

    module.exit_json(**result) 
    #module.fail_json(msg="Unknown error occurred.")

if __name__ == '__main__':
    main()
