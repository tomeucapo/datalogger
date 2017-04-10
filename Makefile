all:		recursos principal llibreta configurador

principal:	gui/f_principal.ui gui/recursos.qrc
		pyuic4 -o frmPrincipal.py -x gui/f_principal.ui

llibreta:	gui/f_llibreta.ui
		pyuic4 -o frmLlibreta.py -x gui/f_llibreta.ui

configurador:	gui/f_principal.ui
		pyuic4 -o frmConfigurador.py -x gui/f_configurador.ui

recursos:	gui/recursos.qrc
		pyrcc4 -o Recursos.py gui/recursos.qrc

clean:		
		rm -f frm*.py frm*.pyc *~ 
		rm -f Recursos.py Recursos.pyc		
