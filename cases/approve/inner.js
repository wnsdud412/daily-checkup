var today = new Date();
var month = (today.getMonth()+1).toString().padStart(2,'0')
var date = (today.getDate()).toString().padStart(2,'0')

HwpCtrl.PutFieldText('doctitle','일일점검_'+month+date+'_내부결재')
HwpCtrl.MoveToField('body',true,true,false)