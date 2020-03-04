class Zinja {
  constructor(vards, zinja, laiks, pupinu=false) {
    this.vards = vards
    this.zinja = zinja
    this.laiks = laiks
    this.pupinu = pupinu
  }

  paraditNoskanojumu = (autoraVards, garastavokli) => {
    if (garastavokli.length == 0) return '-'
    const noskanojums = garastavokli.find(g => g.vards === autoraVards)
    return noskanojums && noskanojums.garastavoklis || '-'
  }

  vaiZinjaIrIzcelta = () => {
    const regExp = new RegExp("^\\*\\*.*\\*\\*$")
    if (!regExp.test(this.zinja)) return false
    this.zinja = this.zinja.split('**')[1]
    return true
  }

  vaiZinjaIrPazinojums = () => {
    const regExp = new RegExp("^!.*!$")
    if (!regExp.test(this.zinja)) return false
    this.zinja = this.zinja.split('!')[1]
    return true
  }

  formateRindu = (garastavokli) => {
    const manasZinjasKlase = this.vards == vards ? 'user' : ''
    const izceltsKlase = this.vaiZinjaIrIzcelta() ? 'izcelts' : ''
    const pazinojumsKlase = this.vaiZinjaIrPazinojums() ? 'pazinojums' : ''

    const noskanojums = this.paraditNoskanojumu(this.vards, garastavokli)
    const laiks = this.laiks ? this.laiks : '-'

    return (
      `<li class='left ${manasZinjasKlase} clearfix'>
        <div class='chat-body ${manasZinjasKlase} ${izceltsKlase} ${pazinojumsKlase} clearfix'>
          ${this.vards} (${noskanojums}): ${this.zinja}, nosūtīts: ${laiks}
        </div>
      </li>`
    )
  }
}
