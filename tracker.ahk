#InstallKeybdHook
#UseHook

$numpad1::
send {enter}/n track top{space}
return

$numpad2::
send {enter}/n track jg{space}
return

$numpad3::
send {enter}/n track mid{space}
return

$numpad4::
send {enter}/n track adc{space}
return

$numpad5::
send {enter}/n track supp{space}
return

$numpad7::
send {enter}/n cdr{space}
return

$numpad8::
send {enter}/n summs{space}
return

$numpad9::
send {enter}%clipboard%{enter}
return

$numpad0::
send {enter}/n summs{enter}
Sleep, 200
send {enter}%clipboard%{enter}
return

return