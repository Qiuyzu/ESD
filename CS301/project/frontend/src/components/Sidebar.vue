<template>
    <aside class="w-64 h-screen bg-gray-900 text-white p-4">
      <ul>
        <li><router-link to="/dashboard" class="block py-2 hover:bg-gray-700">Dashboard</router-link></li>
        <li><router-link to="/clients" class="block py-2 hover:bg-gray-700">Clients</router-link></li>
        <li><router-link to="/accounts" class="block py-2 hover:bg-gray-700">Accounts</router-link></li>
        <li><router-link to="/transactions" class="block py-2 hover:bg-gray-700">Transactions</router-link></li>
      </ul>
    </aside>
  </template>