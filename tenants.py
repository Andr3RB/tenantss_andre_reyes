#este codigo se dedica a generar una lista de inquilinos que luego se puede manipular.

options = 1
list_tenant = []

def create_tenants (tenant_number):
    i = 0
    while i < int(tenant_number):
        list_tenant.append(input("dame el nombre del inquilino " + str(i+1) + " "))
    print("inquilinos creados")

def delete_tenants(id_tenant):
    print("inquilinos creados")

def print_tenants(list_tenant):
    if len(list_tenant) <= 0:
        print("lista vacia")
    else:
        print*list_tenant,sep=""

while options != "0":
    options = input("menu opciones 1. crea inquilinos - 2.borra inquilinos - 3.imprime lista - 0. salir: ")
    if options == "1":
        print("crea inquilinos")
        tenant_number = input("cuantos inquilinos daremos de alta: ")
        create_tenants(tenant_number)
    elif options == "2":
        print_tenants(list_tenant)
        tenant_id = input("selecciona un inquilino para borrar, para borrar ingresa el numero de inquilino arrancando por cero: ")
        delete_tenants(tenant_id)
    elif options == "3":
        print("impresion de lista de inquilinos")
        print_tenants(list_tenant)
    