# PLUGIN MADE BY @IC_X_K FOR @def_Zoka
# Senzir

import random, re
import asyncio
from telethon import events
from zthon import zedub

from ..core.managers import edit_delete, edit_or_reply


@zedub.zed_cmd(pattern="لوف ?(.*)")
async def _(event):
    t = event.pattern_match.group(1)
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
       await event.edit(f"""{t}{t}{t}{t}{t}{t}{t}{t}
{t}{t}{t}{t}{t}{t}{t}{t}
             {t}{t}{t}
             {t}{t}{t}
             {t}{t}{t}
             {t}{t}{t}
             {t}{t}{t}
             {t}{t}{t}
             {t}{t}{t}
             {t}{t}{t} 
             {t}{t}{t}
{t}{t}{t}{t}{t}{t}{t}{t}
{t}{t}{t}{t}{t}{t}{t}{t}\n


{t}{t}
{t}{t}
{t}{t}
{t}{t}
{t}{t}
{t}{t}
{t}{t}
{t}{t}
{t}{t}{t}{t}{t}{t}{t}{t}
{t}{t}{t}{t}{t}{t}{t}{t}\n
⁭
           {t}{t}{t}{t}{t}
      {t}{t}{t}{t}{t}{t}{t}
   {t}{t}                       {t}{t}
 {t}{t}                          {t}{t}
{t}{t}                            {t}{t}
{t}{t}                            {t}{t}
 {t}{t}                           {t}{t}
   {t}{t}                       {t}{t}
       {t}{t}{t}{t}{t}{t}{t}
            {t}{t}{t}{t}{t}\n
⁭
{t}{t}                              {t}{t}
  {t}{t}                          {t}{t}
    {t}{t}                      {t}{t}
      {t}{t}                  {t}{t}
         {t}{t}             {t}{t}
           {t}{t}         {t}{t}
             {t}{t}     {t}{t}
               {t}{t} {t}{t}
                  {t}{t}{t}
                       {t}\n
⁭
{t}{t}{t}{t}{t}{t}{t}{t}
{t}{t}{t}{t}{t}{t}{t}{t}
{t}{t}
{t}{t}
{t}{t}{t}{t}{t}{t}
{t}{t}{t}{t}{t}{t}
{t}{t}
{t}{t}
{t}{t}{t}{t}{t}{t}{t}{t}
{t}{t}{t}{t}{t}{t}{t}{t}\n

{t}{t}                         {t}{t}
  {t}{t}                    {t}{t}
     {t}{t}              {t}{t}
        {t}{t}        {t}{t}
           {t}{t}  {t}{t}
              {t}{t}{t}
                {t}{t}
                {t}{t}
                {t}{t}
                {t}{t}
                {t}{t}\n
⁭
        {t}{t}{t}{t}{t}{t}
     {t}{t}{t}{t}{t}{t}{t}
   {t}{t}                     {t}{t}
 {t}{t}                         {t}{t}
{t}{t}                           {t}{t}
{t}{t}                           {t}{t}
 {t}{t}                         {t}{t}
   {t}{t}                     {t}{t}
      {t}{t}{t}{t}{t}{t}{t}
            {t}{t}{t}{t}{t}\n
⁭
{t}{t}                      {t}{t}
{t}{t}                      {t}{t}
{t}{t}                      {t}{t}
{t}{t}                      {t}{t}
{t}{t}                      {t}{t}
{t}{t}                      {t}{t}
{t}{t}                      {t}{t}
  {t}{t}                  {t}{t}
      {t}{t}{t}{t}{t}{t}
            {t}{t}{t}{t}""")
      

          
