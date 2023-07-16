class Tv {
    constructor () {
        this._relacaoCanal = Array(2,4,6,1)
        this._canalAtivo = 10
        this._volume = 5
    }
    //getters setters
    get canalAtivo() {
        return this._canalAtivo
    }

    set canalAtivo(canal) {
        if (this._relacaoCanal.indexOf(canal) !== -1) {
       this._canalAtivo = canal
        }
    }
}

let tv = new Tv()
console.log(tv.canalAtivo)
tv.canalAtivo = 4
console.log(tv.canalAtivo)