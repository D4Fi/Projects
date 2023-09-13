set complete+=k
set dictionary+=~/configvim/dic

autocmd FileType python source ~/configvim/iabrev/py.vim
autocmd FileType html source ~/configvim/iabrev/html.vim
autocmd FileType javascript source ~/configvim/iabrev/js.vim
autocmd FileType css source ~/configvim/iabrev/css.vim










set colorcolumn=100
set scrolloff=10
"set foldmethod=indent 
set ttyfast
set nowrap
"set ve=all
set smartcase
set autowrite
set number
set mouse=a             
set tabstop=4 
set softtabstop=4 
set shiftwidth=4
set nocompatible
set hlsearch
set ignorecase
set incsearch
set updatetime=100
set encoding=utf-8
set nobackup 
set nowritebackup 
set splitright
set splitbelow
set autoread
syntax on
filetype on
filetype plugin on
filetype indent on


" map #################################################################
nmap <space>e :Ex<cr>
nmap <space>q :wq<cr>
nmap <esc> :w<cr>
"##########################################################################
 
" iabbrev #################################################################
syntax on 
func Main(pat)
	let c = nr2char(getchar(0))
	return (c =~ a:pat) ? '' : c
endfunc

" qwert
iabbrev q = <c-r>=Main('\s')<cr>
iabbrev qe == <c-r>=Main('\s')<cr>
iabbrev ne != <c-r>=Main('\s')<cr>
iabbrev lt < <c-r>=Main('\s')<cr>
iabbrev gt > <c-r>=Main('\s')<cr>
iabbrev ge >= <c-r>=Main('\s')<cr>
iabbrev le <= <c-r>=Main('\s')<cr>

" gfdsa
iabbrev g <bs>:<c-r>=Main('\s')<cr>
iabbrev f <bs>(@)<esc><Home>f@s<c-r>=Main('\s')<cr>
iabbrev d <bs>{@}<esc><Home>f@s<c-r>=Main('\s')<cr>
iabbrev s <bs>'@'<esc><Home>f@s<c-r>=Main('\s')<cr>
iabbrev ss <bs>"@"<esc><Home>f@s<c-r>=Main('\s')<cr>
iabbrev a <bs>[@]<esc><Home>f@s<c-r>=Main('\s')<cr>
iabbrev as <bs><@><esc><Home>f@s<c-r>=Main('\s')<cr>

" bvc<z
iabbrev b <bs>_<c-r>=Main('\s')<cr>
iabbrev bb __@__<esc><Home>f@s<c-r>=Main('\s')<cr>

" django
iabbrev dj {% @ %}<esc><Home>f@s<c-r>=Main('\s')<cr>
"######################################################################
 


"autocomplet
imap a a<c-n><c-p>
imap b b<c-n><c-p>
imap c c<c-n><c-p>
imap d d<c-n><c-p>
imap e e<c-n><c-p>
imap f f<c-n><c-p>
imap g g<c-n><c-p>
imap h h<c-n><c-p>
imap i i<c-n><c-p>
imap j j<c-n><c-p>
imap k k<c-n><c-p>
imap l l<c-n><c-p>
imap m m<c-n><c-p>
imap n n<c-n><c-p>
imap o o<c-n><c-p>
imap p p<c-n><c-p>
imap q q<c-n><c-p>
imap r r<c-n><c-p>
imap s s<c-n><c-p>
imap t t<c-n><c-p>
imap u u<c-n><c-p>
imap v v<c-n><c-p>
imap w w<c-n><c-p>
imap x x<c-n><c-p>
imap y y<c-n><c-p>
imap z z<c-n><c-p>
imap <bs> <bs><c-n><c-p>

"Pmenu config ################################################## 
highlight Pmenu ctermfg=gray ctermbg=black 
highlight PmenuSel ctermfg=black ctermbg=gray
set pumheight=10
"###############################################################
highlight colorcolumn ctermfg=gray ctermbg=233

"Pmenu liha de numeros ################################################## 
"#highlight LineNr ctermfg=gray
"###############################################################
