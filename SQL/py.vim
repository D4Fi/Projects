set complete+=k
set dictionary+=dic

func Eatchar(pat)
	let c = nr2char(getchar(0))
	return (c =~ a:pat) ? '' : c
endfunc

"autocomplet python ###################################################
iabbrev if if @:<esc><Home>f@s<c-r>=Eatchar('\s')<cr>
iabbrev elif elif @:<esc><Home>f@s<c-r>=Eatchar('\s')<cr>
iabbrev else else:<esc><c-r>=Eatchar('\s')<cr>
iabbrev def def @():<esc><Home>f@s<c-r>=Eatchar('\s')<cr>
iabbrev for for i in @:<esc><Home>f@s<c-r>=Eatchar('\s')<cr>
iabbrev while while @:<esc><Home>f@s<c-r>=Eatchar('\s')<cr>
iabbrev class class @:<esc><Home>f@s<c-r>=Eatchar('\s')<cr>
iabbrev from from @ import<esc><Home>f@s<c-r>=Eatchar('\s')<cr>
iabbrev defi def __init__(self,@):<esc><Home>f@s<c-r>=Eatchar('\s')<cr>
iabbrev super super().__init__()<esc><Home>f@s<c-r>=Eatchar('\s')<cr>
iabbrev true True<c-r>=Eatchar('\s')<cr>
iabbrev false False<c-r>=Eatchar('\s')<cr>
iabbrev none None<c-r>=Eatchar('\s')<cr>
iabbrev lambda lambda @:<esc><Home>f@s<c-r>=Eatchar('\s')<cr>

iabbrev defi def __init__(@):<esc><Home>f@s<c-r>=Eatchar('\s')<cr>
iabbrev defstr def __str__(@):<esc><Home>f@s<c-r>=Eatchar('\s')<cr>
iabbrev defrepr def __repr__(@):<esc><Home>f@s<c-r>=Eatchar('\s')<cr>
iabbrev defadd def __add__(@):<esc><Home>f@s<c-r>=Eatchar('\s')<cr>
iabbrev defqe def __qe__(@):<esc><Home>f@s<c-r>=Eatchar('\s')<cr>
iabbrev defpow def __pow__(@):<esc><Home>f@s<c-r>=Eatchar('\s')<cr>
iabbrev defdel def __del__(@):<esc><Home>f@s<c-r>=Eatchar('\s')<cr>
iabbrev deflen def __len__(@):<esc><Home>f@s<c-r>=Eatchar('\s')<cr>
iabbrev defdelet def __delet__(@):<esc><Home>f@s<c-r>=Eatchar('\s')<cr>
iabbrev deflen def __len__(@):<esc><Home>f@s<c-r>=Eatchar('\s')<cr>
iabbrev defne def __ne__(@):<esc><Home>f@s<c-r>=Eatchar('\s')<cr>
iabbrev defgt def __gt__(@):<esc><Home>f@s<c-r>=Eatchar('\s')<cr>
iabbrev deflt def __lt__(@):<esc><Home>f@s<c-r>=Eatchar('\s')<cr>
iabbrev defge def __ge__(@):<esc><Home>f@s<c-r>=Eatchar('\s')<cr>
iabbrev defle def __le__(@):<esc><Home>f@s<c-r>=Eatchar('\s')<cr>
