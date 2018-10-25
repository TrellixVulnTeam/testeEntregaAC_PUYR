from django import forms


class ContatoForm(forms.Form):

    email = forms.EmailField()
    nome = forms.CharField()
    mensagem = forms.CharField()

    def is_valid(self):
        valido = super(ContatoForm, self).is_valid()
        if valido:
            self.enviar_email()
        return valido


    def enviar_email(self):
        print("Nome: "+self.cleaned_data["nome"])
        print("E-mail: "+self.cleaned_data["email"])
        print("Mensagem:")
        print(self.cleaned_data["mensagem"])

class LoginForm(forms.Form):
    usuario = forms.CharField()
    senha = forms.CharField()

    def is_valid(self):
        
        valido = super(LoginForm, self).is_valid()
        
        if valido:
            self.logar()
        return valido

    def logar(self):
        print("Usuário: "+self.cleaned_data["usuario"])
        print("Senha: "+self.cleaned_data["senha"])
        