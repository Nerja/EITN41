# B-1

## Assignment text:
SAML assertions, which are formatted using XML, are digitally signed by the IdP. For this, and other similar purposes, there is a recommendation by IETF and W3C on how to combine signatures with XML. This is called XML Signatures. Read about and understand XML Signatures. Make sure that you get an overview of the <signature> tag and its contents, as well as the difference between enveloped, enveloping and detached signatures.

### Assessment:
There will be two Moodle-questions on XML signatures. One is general with a focus on under- standing the different parts of the <signature> tag and one is focused on the difference between enveloped, enveloping and detached signatures. Though you are not supposed to know the details, it can be a good idea to have the specification accessible when you answer the questions. You need to correctly answer both questions in order to pass. Note that the second question can have more than one correct alternative. Both students must finish the quiz.

## Notes

* XML Signatures: Recommentation how to combine XML and signatures
* Anything accessible via URL can be signed
* Different types:
	* Detached signature: Used to sign a resouce outside its containing XML document
	* Enveloped signature: Used to sign some part of its containing XML document
	* Enveloping signature: Contains signed data within itself
* \<signature\> tag: 
	* Basic structure:
	   ```
	   <Signature>
	   		<SignedInfo>
	   			<CanonicalizationMethod />
	   			<SignatureMethod />
	   			<Reference>
	   				<Transforms />
	   				<DigestMethod />
	   				<DigestValue />
	   			</Reference>
	   			<Reference>
	   			...
	   			</Reference>
	   		</SignedInfo>
	   		<SignatureValue />
	   		<KeyInfo />
	   		</Object />
	   dafuck
	   </Signature>
	   ```
	* Structure description:
		* SignedInfo contains elements/references to signed data and algorithms
* Core Validation  is used to validating a XML signature. Watch out for signature wrapping attacks.
* Hard since XML more than one legal serialized reprensentation(CR-> CR LF)
* XML canon applied produce same serialized reprensentations
* XML signatures more flexible than PGP, ..