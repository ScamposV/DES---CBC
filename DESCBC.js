// ==UserScript==
// @name         Script cifrado
// @namespace    http://tampermonkey.net/
// @version      0.1
// @updateURL    https://github.com/ScamposV/DES-CBC/blob/asd/DESCBC.js
// @description  try to take over the world!
// @author       You
// @match        file:///C:/Users/Tat%C3%A1n/index.html
// @icon         https://www.google.com/s2/favicons?domain=google.com
// @grant        none
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.0.0/crypto-js.min.js
// ==/UserScript==

//const CryptoJS = require('crypto-js')

const keyHex = CryptoJS.enc.Utf8.parse(document.getElementsByClassName('key')[0].id)
const iv1 = document.getElementsByClassName('iv')[0].id;
const mensaje = document.getElementsByClassName('DESCBC')[0].id;

var iv2=CryptoJS.enc.Utf8.parse(iv1);

/*
//Visualizacion de las variables obtenidas y modificadas
console.log(keyHex, iv2, mensaje)*/

var decoded = CryptoJS.DES.decrypt(
	{ciphertext: CryptoJS.enc.Hex.parse(document.getElementsByClassName('DESCBC')[0].id)},
	keyHex,{
		iv: iv2,
		mode: CryptoJS.mode.CBC,
		padding: CryptoJS.pad.NoPadding});
console.log(decoded.toString(CryptoJS.enc.Utf8))
